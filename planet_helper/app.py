"""Tkinter user interface. Read-only guide: it never touches the game, its files, or the network."""
from __future__ import annotations

import tkinter as tk
import webbrowser
from datetime import datetime, timezone
from tkinter import font as tkfont
from tkinter import ttk

from . import __version__
from .data import ACTIVITY_TYPES, STAGES, Dataset
from .ranking import AVAILABLE, BLOCKED, COOLDOWN, DONE, ranked
from .store import Progress

# High-contrast dark palette (text/background contrast > 12:1).
BG, PANEL, FG, MUTED = "#0f1419", "#182028", "#f4f6f8", "#c3ccd5"
ACCENT, WARN, OK, BAD, LINK = "#ffd166", "#ffb347", "#7ee081", "#ff8a80", "#8ecbff"
SEL = "#2d5d8a"

VIEWS = {
    "Next actions": {AVAILABLE},
    "Everything": {AVAILABLE, COOLDOWN, BLOCKED, DONE},
    "Cooling down": {COOLDOWN},
    "Blocked (needs something first)": {BLOCKED},
    "Done": {DONE},
}
STATE_LABEL = {AVAILABLE: "Ready", COOLDOWN: "Cooling down", BLOCKED: "Blocked", DONE: "Done"}
PREREQ_SHORT = {"verified": "Checked", "partial": "Partly known", "unknown": "Unknown", "unreviewed": "Not checked"}
PREREQ_HEADLINE = {
    "verified": "✔ Checked against sources: this is the full list as far as the sources show.",
    "partial": "◐ Partly known: the items below are sourced, but something may be missing (see Unknown).",
    "unknown": "? Unknown: no source says what is needed first. An empty list does NOT mean nothing is needed.",
    "unreviewed": "… Not checked yet: nobody has verified prerequisites for this entry. An empty list does NOT mean nothing is needed.",
}
TYPE_LABEL = {t: t.replace("-", " ").capitalize() for t in ACTIVITY_TYPES}
SAFETY = ("Manual planet choice. This app does not read the game, its memory, logs or chat, sends nothing "
          "over the network, and never presses keys for you. Progress is stored only on this PC.")


def _local(dt: datetime) -> str:
    return dt.astimezone().strftime("%a %d %b %H:%M")


class PlanetHelperApp:
    def __init__(self, root: tk.Tk, dataset: Dataset, progress: Progress, start_planet: str | None = None):
        self.root, self.ds, self.progress = root, dataset, progress
        progress.adopt_former_ids(dataset.former_ids)   # merged entries keep what you already ticked
        self.rows: list = []
        self.base_size = int(progress.settings.get("fontSize", 11))
        root.title("Entropia Planet Helper")
        root.geometry("1280x820")
        root.minsize(900, 600)
        root.configure(bg=BG)
        self._fonts()
        self._style()

        order = sorted(dataset.planets, key=lambda p: (dataset.planets[p]["planet"]["status"] != "active",
                                                       dataset.planets[p]["planet"]["name"].lower()))
        self.planet_ids = order
        initial = start_planet or progress.settings.get("planet")
        if initial not in dataset.planets:
            initial = "aris" if "aris" in dataset.planets else (order[0] if order else None)
        self.planet = tk.StringVar(value=initial or "")
        self.stage = tk.StringVar(value=progress.settings.get("stage", "arrival")
                                  if progress.settings.get("stage") in STAGES else "arrival")
        self.budget = tk.BooleanVar(value=bool(progress.settings.get("budgetMode", False)))
        self.view = tk.StringVar(value="Next actions")
        self.type_filter = tk.StringVar(value="All types")
        self.query = tk.StringVar()
        self._build()
        self._bind_keys()
        if initial:
            self.planet_box.current(order.index(initial))
        self.on_planet_change()
        if progress.recovered_from:
            self.flash(f"Progress file was damaged; kept a copy at {progress.recovered_from} and started fresh.")

    # ----------------------------------------------------------------- setup
    def _fonts(self):
        s = self.base_size
        self.f_body = tkfont.Font(family="Segoe UI", size=s)
        self.f_bold = tkfont.Font(family="Segoe UI", size=s, weight="bold")
        self.f_h1 = tkfont.Font(family="Segoe UI", size=s + 7, weight="bold")
        self.f_h2 = tkfont.Font(family="Segoe UI", size=s + 3, weight="bold")
        self.f_mono = tkfont.Font(family="Consolas", size=s)

    def _resize(self, delta: int):
        self.base_size = max(8, min(22, self.base_size + delta))
        for f, extra in ((self.f_body, 0), (self.f_bold, 0), (self.f_h1, 7), (self.f_h2, 3), (self.f_mono, 0)):
            f.configure(size=self.base_size + extra)
        ttk.Style().configure("Treeview", rowheight=int(self.base_size * 2.4))
        self.progress.set_setting("fontSize", self.base_size)

    def _style(self):
        st = ttk.Style()
        st.theme_use("clam")
        st.configure(".", background=BG, foreground=FG, fieldbackground=PANEL, font=self.f_body)
        st.configure("TLabel", background=BG, foreground=FG)
        st.configure("Muted.TLabel", foreground=MUTED)
        st.configure("H1.TLabel", font=self.f_h1, foreground=ACCENT)
        st.configure("Warn.TLabel", foreground=WARN)
        st.configure("TFrame", background=BG)
        st.configure("Panel.TFrame", background=PANEL)
        st.configure("TCheckbutton", background=BG, foreground=FG)
        st.map("TCheckbutton", background=[("active", BG)])
        st.configure("TButton", background="#26313c", foreground=FG, padding=(10, 5), borderwidth=1)
        st.map("TButton", background=[("active", SEL), ("disabled", "#1b232b")],
               foreground=[("disabled", "#7d8892")])
        st.configure("Accent.TButton", background="#3b6e3e")
        st.configure("TCombobox", fieldbackground=PANEL, background="#26313c", foreground=FG,
                     arrowcolor=FG, selectbackground=SEL, selectforeground=FG)
        st.map("TCombobox", fieldbackground=[("readonly", PANEL)], foreground=[("readonly", FG)])
        st.configure("TEntry", fieldbackground=PANEL, foreground=FG, insertcolor=FG)
        st.configure("Treeview", background=PANEL, fieldbackground=PANEL, foreground=FG,
                     rowheight=int(self.base_size * 2.4), font=self.f_body, borderwidth=0)
        st.configure("Treeview.Heading", background="#26313c", foreground=FG, font=self.f_bold)
        st.map("Treeview", background=[("selected", SEL)], foreground=[("selected", "#ffffff")])
        self.root.option_add("*TCombobox*Listbox.background", PANEL)
        self.root.option_add("*TCombobox*Listbox.foreground", FG)
        self.root.option_add("*TCombobox*Listbox.selectBackground", SEL)
        self.root.option_add("*TCombobox*Listbox.font", self.f_body)

    def _build(self):
        top = ttk.Frame(self.root, padding=(12, 10, 12, 4))
        top.pack(fill="x")
        ttk.Label(top, text="Destination", style="Muted.TLabel").grid(row=0, column=0, sticky="w")
        labels = []
        for pid in self.planet_ids:
            p = self.ds.planets[pid]["planet"]
            labels.append(p["name"] if p["status"] == "active" else f"{p['name']} ({p['status']})")
        self.planet_box = ttk.Combobox(top, values=labels, state="readonly", width=26, font=self.f_body)
        self.planet_box.grid(row=1, column=0, sticky="w", padx=(0, 14))
        self.planet_box.bind("<<ComboboxSelected>>", lambda e: self._pick_planet())

        ttk.Label(top, text="Your stage here", style="Muted.TLabel").grid(row=0, column=1, sticky="w")
        stage_box = ttk.Combobox(top, values=[s.capitalize() for s in STAGES], state="readonly", width=10,
                                 font=self.f_body)
        stage_box.current(STAGES.index(self.stage.get()))
        stage_box.grid(row=1, column=1, sticky="w", padx=(0, 14))
        stage_box.bind("<<ComboboxSelected>>", lambda e: self._set_stage(STAGES[stage_box.current()]))

        ttk.Label(top, text="Show", style="Muted.TLabel").grid(row=0, column=2, sticky="w")
        view_box = ttk.Combobox(top, values=list(VIEWS), textvariable=self.view, state="readonly", width=28,
                                font=self.f_body)
        view_box.grid(row=1, column=2, sticky="w", padx=(0, 14))
        view_box.bind("<<ComboboxSelected>>", lambda e: self.refresh())

        ttk.Label(top, text="Type", style="Muted.TLabel").grid(row=0, column=3, sticky="w")
        type_box = ttk.Combobox(top, values=["All types"] + [TYPE_LABEL[t] for t in sorted(ACTIVITY_TYPES)],
                                textvariable=self.type_filter, state="readonly", width=14, font=self.f_body)
        type_box.grid(row=1, column=3, sticky="w", padx=(0, 14))
        type_box.bind("<<ComboboxSelected>>", lambda e: self.refresh())

        ttk.Label(top, text="Search (Ctrl+F)", style="Muted.TLabel").grid(row=0, column=4, sticky="w")
        self.search = ttk.Entry(top, textvariable=self.query, width=24, font=self.f_body)
        self.search.grid(row=1, column=4, sticky="we", padx=(0, 14))
        self.query.trace_add("write", lambda *a: self.refresh())
        ttk.Checkbutton(top, text="Budget mode (favour cheap)", variable=self.budget,
                        command=self._set_budget).grid(row=1, column=5, sticky="w")
        top.columnconfigure(4, weight=1)

        hdr = ttk.Frame(self.root)
        hdr.pack(fill="x")
        self.header = tk.Text(hdr, height=5, wrap="word", bg=BG, fg=FG, relief="flat",
                              font=self.f_body, padx=12, pady=4, cursor="arrow", highlightthickness=0)
        hsb = ttk.Scrollbar(hdr, orient="vertical", command=self.header.yview)
        self.header.configure(yscrollcommand=hsb.set)
        self.header.pack(side="left", fill="x", expand=True)
        hsb.pack(side="right", fill="y")
        self._text_tags(self.header)

        body = ttk.PanedWindow(self.root, orient="horizontal")
        body.pack(fill="both", expand=True, padx=12, pady=6)
        left = ttk.Frame(body)
        cols = ("rank", "title", "type", "stage", "status", "prereqs", "score")
        self.tree = ttk.Treeview(left, columns=cols, show="headings", selectmode="browse")
        for c, w, txt in (("rank", 36, "#"), ("title", 230, "Activity"), ("type", 90, "Type"),
                          ("stage", 64, "Stage"), ("status", 110, "Status"), ("prereqs", 105, "Prereqs"),
                          ("score", 52, "Score")):
            self.tree.heading(c, text=txt)
            self.tree.column(c, width=w, minwidth=w if c != "title" else 140, stretch=(c == "title"), anchor="w")
        sb = ttk.Scrollbar(left, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        self.tree.bind("<<TreeviewSelect>>", lambda e: self.show_detail())
        self.tree.tag_configure(COOLDOWN, foreground=WARN)
        self.tree.tag_configure(BLOCKED, foreground=MUTED)
        self.tree.tag_configure(DONE, foreground=OK)
        body.add(left, weight=3)

        right = ttk.Frame(body)
        btns = ttk.Frame(right)
        btns.pack(fill="x", pady=(0, 6))
        self.b_done = ttk.Button(btns, text="Mark done (D)", style="Accent.TButton", command=self.mark_done)
        self.b_ready = ttk.Button(btns, text="Ready again", command=self.ready_again)
        self.b_undo = ttk.Button(btns, text="Undo / not done", command=self.undo)
        for b in (self.b_done, self.b_ready, self.b_undo):
            b.pack(side="left", padx=(0, 6))
        ttk.Button(btns, text="About this destination", command=self.show_about).pack(side="right")
        self.detail = tk.Text(right, wrap="word", bg=PANEL, fg=FG, relief="flat", font=self.f_body,
                              padx=14, pady=10, highlightthickness=0, cursor="arrow")
        dsb = ttk.Scrollbar(right, orient="vertical", command=self.detail.yview)
        self.detail.configure(yscrollcommand=dsb.set)
        self.detail.pack(side="left", fill="both", expand=True)
        dsb.pack(side="right", fill="y")
        self._text_tags(self.detail)
        body.add(right, weight=4)

        self.status = ttk.Label(self.root, style="Muted.TLabel", padding=(12, 2, 12, 8), wraplength=1200)
        self.status.pack(fill="x")

    def _text_tags(self, t: tk.Text):
        t.tag_configure("h1", font=self.f_h1, foreground=ACCENT, spacing3=4)
        t.tag_configure("h2", font=self.f_h2, foreground=ACCENT, spacing1=10, spacing3=3)
        t.tag_configure("b", font=self.f_bold)
        t.tag_configure("muted", foreground=MUTED)
        t.tag_configure("warn", foreground=WARN)
        t.tag_configure("ok", foreground=OK)
        t.tag_configure("bad", foreground=BAD)
        t.tag_configure("mono", font=self.f_mono, foreground="#ffffff", background="#26313c")
        t.tag_configure("bullet", lmargin1=14, lmargin2=30, spacing1=2)
        t.tag_configure("link", foreground=LINK, underline=True)
        t.tag_bind("link", "<Enter>", lambda e, w=t: w.configure(cursor="hand2"))
        t.tag_bind("link", "<Leave>", lambda e, w=t: w.configure(cursor="arrow"))

    def _bind_keys(self):
        self.root.bind("<Control-f>", lambda e: (self.search.focus_set(), "break"))
        self.root.bind("<Control-equal>", lambda e: self._resize(1))
        self.root.bind("<Control-plus>", lambda e: self._resize(1))
        self.root.bind("<Control-minus>", lambda e: self._resize(-1))
        self.tree.bind("d", lambda e: self.mark_done())
        self.root.bind("<Escape>", lambda e: self.query.set(""))

    # ---------------------------------------------------------- settings
    def _pick_planet(self):
        self.planet.set(self.planet_ids[self.planet_box.current()])
        self.on_planet_change()

    def _set_stage(self, stage: str):
        self.stage.set(stage)
        self.progress.set_setting("stage", stage)
        self.refresh()

    def _set_budget(self):
        self.progress.set_setting("budgetMode", bool(self.budget.get()))
        self.refresh()

    def on_planet_change(self):
        pid = self.planet.get()
        if not pid:
            self._write(self.header, [("No destination data found. Check the data folder.", "bad")])
            return
        self.progress.set_setting("planet", pid)
        doc = self.ds.planets[pid]
        p = doc["planet"]
        self.root.title(f"Entropia Planet Helper - {p['name']}")
        nwarn = len(p["warnings"])
        parts = [(p["name"], "h1"), (f"   {p['status'].upper()} · {p['kind']} · reviewed {p['lastReviewed']}   ", "muted")]
        if nwarn:
            parts.append((f"⚠ {nwarn} caution{'s' if nwarn != 1 else ''}: press 'About this destination'\n", "warn"))
        else:
            parts.append(("\n", None))
        parts += [(p["summary"] + "\n", None), ("Getting there: ", "b"), (p["howToReach"], None)]
        self._write(self.header, parts)
        self.header.yview_moveto(0)
        self.refresh()

    # ------------------------------------------------------------ list
    def current_rows(self):
        pid = self.planet.get()
        acts = [a for a in self.ds.activities.values() if a["_planet"] == pid]
        rows = ranked(acts, self.progress, self.stage.get(), self.budget.get())
        tf = self.type_filter.get()
        q = self.query.get().strip().lower()
        # A search looks everywhere, so a stuck player finds blocked or done items without changing "Show".
        allowed = VIEWS["Everything"] if q else VIEWS[self.view.get()]
        out = []
        for row in rows:
            act, st = row[0], row[1]
            if st.state not in allowed:
                continue
            if tf != "All types" and TYPE_LABEL[act["type"]] != tf:
                continue
            if q:
                hay = " ".join([act["title"], act["summary"], " ".join(act["tags"]), " ".join(act["steps"]),
                                " ".join(act["rewards"]), " ".join(l["label"] for l in act["locations"]),
                                " ".join(act["requirementsText"]), act["prereqInfo"]["note"],
                                " ".join(d["symptom"] + " " + d["check"] for d in act.get("diagnostics", []))]).lower()
                if not all(word in hay for word in q.split()):
                    continue
            out.append(row)
        return out

    def refresh(self):
        keep = self.tree.selection()
        keep = keep[0] if keep else None
        self.rows = self.current_rows()
        self.tree.delete(*self.tree.get_children())
        for i, (act, st, sc, _) in enumerate(self.rows, 1):
            label = STATE_LABEL[st.state]
            if st.state == COOLDOWN and st.ready_at:
                label = f"Ready {_local(st.ready_at)}"
            self.tree.insert("", "end", iid=act["id"], tags=(st.state,),
                             values=(i, act["title"], TYPE_LABEL[act["type"]], act["stage"].capitalize(), label,
                                     PREREQ_SHORT[act["prereqInfo"]["status"]], f"{sc:g}"))
        if keep and self.tree.exists(keep):
            self.tree.selection_set(keep)
        elif self.rows:
            self.tree.selection_set(self.rows[0][0]["id"])
        else:
            self._write(self.detail, [("Nothing to show here.", "h2"),
                                      ("\nTry 'Everything' under Show, clear the search (Esc), or pick another type.", "muted")])
            self._buttons(None)
        self._update_status()

    def _update_status(self):
        pid = self.planet.get()
        all_acts = [a for a in self.ds.activities.values() if a["_planet"] == pid]
        counts = {s: 0 for s in STATE_LABEL}
        for _, st, _, _ in ranked(all_acts, self.progress, self.stage.get(), self.budget.get()):
            counts[st.state] += 1
        self.status.configure(foreground=MUTED, text=(f"{len(all_acts)} activities here: {counts[AVAILABLE]} ready, {counts[COOLDOWN]} cooling down, "
                                    f"{counts[BLOCKED]} blocked, {counts[DONE]} done.   Progress file: {self.progress.path}   "
                                    f"v{__version__}.   {SAFETY}"))

    # ---------------------------------------------------------- detail
    def selected(self):
        sel = self.tree.selection()
        if not sel:
            return None
        return next((r for r in self.rows if r[0]["id"] == sel[0]), None)

    def show_detail(self):
        row = self.selected()
        self._buttons(row)
        if not row:
            return
        act, st, sc, why = row
        planet_doc = self.ds.planets[act["_planet"]]
        srcs = {s["id"]: s for s in planet_doc["sources"]}
        t = self.detail
        t.configure(state="normal")
        t.delete("1.0", "end")
        self._links = {}
        t.insert("end", act["title"] + "\n", "h1")
        t.insert("end", f"{TYPE_LABEL[act['type']]} · {act['stage']} stage · confidence {act['confidence']} · "
                        f"last verified {act['lastVerified']}\n", "muted")
        state_tag = {AVAILABLE: "ok", COOLDOWN: "warn", BLOCKED: "bad", DONE: "ok"}[st.state]
        msg = STATE_LABEL[st.state]
        if st.state == COOLDOWN:
            msg += f": ready again {_local(st.ready_at)} (your local time). " if st.ready_at else ". "
            msg += st.note
        elif st.state == BLOCKED:
            names = [self.ds.activities[m]["title"] if m in self.ds.activities else m for m in st.missing]
            msg += ": first finish " + "; ".join(names)
        elif st.note:
            msg += ". " + st.note
        rec = self.progress.records.get(act["id"])
        if rec and rec.get("count"):
            msg += f"  (marked done {rec['count']}x"
            last = self.progress.last_done(act["id"])
            msg += f", last {_local(last)})" if last else ")"
        t.insert("end", msg + "\n", state_tag)
        t.insert("end", act["summary"] + "\n", None)
        for w in act["warnings"]:
            t.insert("end", "⚠ " + w + "\n", "warn")
        if act.get("diagnostics"):
            t.insert("end", "Stuck? Check these in order\n", "h2")
            for i, d in enumerate(act["diagnostics"], 1):
                t.insert("end", f"{i}. {d['symptom']}\n", ("bullet", "b"))
                t.insert("end", f"    {d['check']}\n", "bullet")
                names = "; ".join(srcs[s]["title"] for s in d["sourceIds"])
                t.insert("end", f"    Source: {names}\n", ("bullet", "muted"))
        self._prereq_section(t, act)
        if act.get("unknowns"):
            t.insert("end", "Not known yet (no source found)\n", "h2")
            for u in act["unknowns"]:
                t.insert("end", f"?  {u}\n", ("bullet", "muted"))

        t.insert("end", "Why it is ranked here\n", "h2")
        t.insert("end", act["score"]["rationale"] + "\n", None)
        t.insert("end", why + "\n", "muted")
        self._list(t, "Steps", act["steps"], numbered=True)
        self._list(t, "Rewards", act["rewards"])
        c = act["cost"]
        t.insert("end", "Cost\n", "h2")
        est = "unknown" if c["pedEstimate"] is None else f"about {c['pedEstimate']:g} PED"
        t.insert("end", f"Estimate: {est}. {c['text']}\n", None)
        t.insert("end", f"Markup: {c['markup']}. {c['markupNote']}\n", "muted")
        if act["currencies"]:
            t.insert("end", "Currencies / tokens\n", "h2")
            for cur in act["currencies"]:
                t.insert("end", f"•  {cur['name']} ({cur['use']}): {cur['note']}\n", "bullet")
        t.insert("end", "Limits and cooldown\n", "h2")
        if act["limits"]:
            t.insert("end", act["limits"] + "\n", None)
        cd = act["cooldown"]
        cdtxt = {"none": "No cooldown.", "once": "One-time.", "rolling": f"Repeatable every {cd.get('hours') or '?'} h (timer starts when you mark it done).",
                 "fixed-reset": "Resets at a fixed time.", "unknown": "Reset timing not confirmed."}[cd["kind"]]
        t.insert("end", f"{cdtxt} {cd['resetNote']}\n", "muted")
        if act["locations"]:
            t.insert("end", "Where\n", "h2")
            for loc in act["locations"]:
                t.insert("end", f"•  {loc['label']}", "bullet")
                if loc["waypoint"]:
                    t.insert("end", "\n    ")
                    t.insert("end", f" /wp {loc['waypoint']} ", "mono")
                    btn = tk.Button(t, text="Copy", command=lambda w=loc["waypoint"]: self.copy_wp(w),
                                    bg="#26313c", fg=FG, activebackground=SEL, activeforeground=FG,
                                    relief="flat", font=self.f_body, padx=8, cursor="hand2")
                    t.window_create("end", window=btn, padx=6)
                    t.insert("end", "  verified by source" if loc["verified"] else "  NOT verified - check in game",
                             "ok" if loc["verified"] else "warn")
                t.insert("end", "\n")
        t.insert("end", "Sources\n", "h2")
        for sid in act["sourceIds"]:
            self._source_line(t, srcs[sid])
        if act["tags"]:
            t.insert("end", "\nTags: " + ", ".join(act["tags"]) + "\n", "muted")
        t.configure(state="disabled")

    def show_about(self):
        """Full destination info: summary, travel, every caution and the destination-level sources."""
        pid = self.planet.get()
        if not pid:
            return
        self.tree.selection_remove(*self.tree.selection())
        self._buttons(None)
        doc = self.ds.planets[pid]
        p = doc["planet"]
        srcs = {s["id"]: s for s in doc["sources"]}
        t = self.detail
        t.configure(state="normal")
        t.delete("1.0", "end")
        t.insert("end", f"About {p['name']}\n", "h1")
        parent = self.ds.planets.get(p["parent"], {}).get("planet", {}).get("name", p["parent"]) if p["parent"] else None
        t.insert("end", f"{p['kind']} · status {p['status']}" + (f" · part of {parent}" if parent else "")
                 + f" · reviewed {p['lastReviewed']} · {len(doc['activities'])} activities, {len(doc['sources'])} sources\n", "muted")
        t.insert("end", p["summary"] + "\n")
        t.insert("end", "Getting there\n", "h2")
        t.insert("end", p["howToReach"] + "\n")
        if p["warnings"]:
            t.insert("end", "Cautions\n", "h2")
            for w in p["warnings"]:
                t.insert("end", "⚠  " + w + "\n", ("bullet", "warn"))
        t.insert("end", "Main sources for this destination\n", "h2")
        for sid in p["sourceIds"]:
            self._source_line(t, srcs[sid])
        t.insert("end", "\nEvery activity lists its own sources. The README has the full list.\n", "muted")
        t.configure(state="disabled")

    def _prereq_section(self, t, act):
        """Always shown: what must be done first, and how sure we are about that list."""
        pi = act["prereqInfo"]
        t.insert("end", "Before you start (prerequisites)\n", "h2")
        tag = {"verified": "ok", "partial": "warn", "unknown": "warn", "unreviewed": "muted"}[pi["status"]]
        t.insert("end", PREREQ_HEADLINE[pi["status"]] + "\n", tag)
        if pi["note"]:
            t.insert("end", pi["note"] + "\n")
        for p in act["prerequisites"]:
            pa = self.ds.activities.get(p)
            done = self.progress.ever_done(p)
            where = "" if not pa or pa["_planet"] == act["_planet"] else f" ({self.ds.planets[pa['_planet']]['planet']['name']})"
            if pa and pa["type"] == "travel" and not done:
                t.insert("end", f"↪  {pa['title']}{where} (travel step; does not block)\n", ("bullet", "muted"))
                continue
            t.insert("end", f"{'✔' if done else '✗'}  {pa['title'] if pa else p}{where}\n",
                     ("bullet", "ok" if done else "bad"))
        for r in act["requirementsText"]:
            t.insert("end", f"•  {r}\n", "bullet")
        for u in pi["unknowns"]:
            t.insert("end", f"?  Unknown: {u}\n", ("bullet", "muted"))

    def _source_line(self, t, s):
        tag = f"link-{s['id']}"
        t.insert("end", "•  ", "bullet")
        t.insert("end", s["title"], ("link", tag))
        t.tag_bind(tag, "<Button-1>", lambda e, u=s["url"]: webbrowser.open(u))
        t.insert("end", f"  ({s['publisher']}, {s['kind']}, published {s['published'] or 'undated'}, "
                        f"checked {s['accessed']})\n", "muted")
        t.insert("end", f"    {s['supports']}\n", "muted")

    def _list(self, t, title, items, numbered=False):
        if not items:
            return
        t.insert("end", title + "\n", "h2")
        for i, it in enumerate(items, 1):
            t.insert("end", (f"{i}. " if numbered else "•  ") + it + "\n", "bullet")

    def _write(self, t: tk.Text, parts):
        t.configure(state="normal")
        t.delete("1.0", "end")
        for text, tag in parts:
            t.insert("end", text, tag) if tag else t.insert("end", text)
        t.configure(state="disabled")

    def _buttons(self, row):
        if not row:
            for b in (self.b_done, self.b_ready, self.b_undo):
                b.state(["disabled"])
            return
        act, st = row[0], row[1]
        rec = self.progress.records.get(act["id"])
        self.b_done.state(["!disabled"] if st.state in (AVAILABLE, BLOCKED) else ["disabled"])
        self.b_ready.state(["!disabled"] if st.state == COOLDOWN else ["disabled"])
        self.b_undo.state(["!disabled"] if rec else ["disabled"])

    # --------------------------------------------------------- actions
    def _act_on(self, fn):
        row = self.selected()
        if not row:
            return
        fn(row[0]["id"])
        self.refresh()
        if self.tree.exists(row[0]["id"]):
            self.tree.selection_set(row[0]["id"])
        self.show_detail()

    def mark_done(self):
        row = self.selected()
        if row and row[1].state in (AVAILABLE, BLOCKED):
            self._act_on(self.progress.mark_done)
            self.flash(f"Marked done: {row[0]['title']}")

    def ready_again(self):
        self._act_on(self.progress.ready_again)

    def undo(self):
        self._act_on(self.progress.undo)

    def copy_wp(self, wp: str):
        self.root.clipboard_clear()
        self.root.clipboard_append(f"/wp {wp}")
        self.flash(f"Copied: /wp {wp}  (paste it into the in-game chat yourself)")

    def flash(self, msg: str):
        self.status.configure(text=msg, foreground=ACCENT)
        self.root.after(4000, lambda: (self.status.configure(foreground=MUTED), self._update_status()))


def run(dataset: Dataset, progress: Progress, start_planet: str | None = None) -> None:
    root = tk.Tk()
    try:
        root.tk.call("tk", "scaling", root.winfo_fpixels("1i") / 72.0)
    except tk.TclError:
        pass
    PlanetHelperApp(root, dataset, progress, start_planet)
    root.mainloop()
