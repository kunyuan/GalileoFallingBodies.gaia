"""Galileo's Falling Bodies — re-formalization following theory doc §3.

Source: docs/foundations/theory/05-formalization-methodology.md §3.1
Original texts: Aristotle De Caelo I.6, Galileo Discorsi (1638)

Pass 4: Refined strategy types.
  W₁  abduction(obs_daily → A)
  W₂a induction([obs_media, obs_air] → G)
  W₂b deduction(G → V)
  W₃  deduction(V → predictions) + equivalence(pred ≡ obs)
  Deterministic derivations: deduction
  Contradictions: T₁⊗T₂, A_vac⊗V
"""

from gaia.lang import (
    abduction,
    claim,
    contradiction,
    deduction,
    equivalence,
    induction,
    noisy_and,
    setting,
)

# ═══════════════════════════════════════════════════════════════════════
# Settings — background context, no probability
# ═══════════════════════════════════════════════════════════════════════

vacuum = setting(
    "真空是完全没有阻力的理想化环境：介质密度为零，唯一作用力为重力。"
)

inclined_plane = setting(
    "伽利略斜面实验装置：12 腕尺长的抛光木条沟槽，"
    "衬以光滑羊皮纸，使用坚硬光滑的青铜球——"
    "摩擦和空气阻力可忽略，近似纯重力环境。"
)

# ═══════════════════════════════════════════════════════════════════════
# Observations — empirical evidence (leaf claims)
# ═══════════════════════════════════════════════════════════════════════

obs_daily = claim(
    "日常经验中，较重的物体下落速度确实比较轻的物体快："
    "石头比羽毛快，铁球比木球快。",
    title="Daily Observation",
)

obs_media = claim(
    "在不同密度的介质中比较不同重量物体的下落："
    "介质越稠密（如水银、水、油），轻重物体的速度差异越大；"
    "介质越稀薄（如空气），差异越小。"
    "在水银中，金是唯一能下沉的物质，其他金属和石头都浮在表面。",
    title="Media Observation",
)

obs_air = claim(
    "在空气中做精细实验：金球、铅球、铜球、斑岩球等重材料球"
    "从 100 腕尺高处落下，金球领先铜球不超过四指宽。",
    title="Air Experiment",
)

obs_theta1 = claim(
    "斜面实验第一组：在倾角 θ₁ 下，不同重量的光滑青铜球"
    "沿抛光沟槽滚下，所经距离之比等于时间之比的平方，"
    "与球的重量无关。",
    title="Inclined Plane θ₁",
)

obs_theta2 = claim(
    "斜面实验第二组：在另一倾角 θ₂ 下重复实验，结果一致确认"
    "距离 ∝ 时间²，与重量无关。实验重复整整一百次，"
    "对所有倾角均成立。",
    title="Inclined Plane θ₂",
)

# ═══════════════════════════════════════════════════════════════════════
# Hypotheses — central claims under test
# ═══════════════════════════════════════════════════════════════════════

hyp_aristotle = claim(
    "物体的下落速度与其重量成正比：一个重量是另一个两倍的物体，"
    "通过同样距离所需时间为后者的一半。即重物比轻物下落更快。",
    title="Aristotle's Law",
)

hyp_air_resistance = claim(
    "不同重量物体的下落速度差异完全由介质阻力造成——"
    "阻力是速度差异的唯一原因。"
    "阻力越大，差异越大；阻力越小，差异越小。",
    title="Air Resistance Hypothesis",
)

hyp_vacuum_equal = claim(
    "在完全没有阻力的介质（真空）中，"
    "不同重量的物体以相同速率下落。",
    title="Vacuum Equal Speed",
)

# ═══════════════════════════════════════════════════════════════════════
# Derived claims
# ═══════════════════════════════════════════════════════════════════════

hyp_drag = claim(
    "在亚里士多德定律下，将重球 H（速度 8）与轻球 L（速度 4）绑在一起，"
    "L 对 H 产生拖拽，复合体 HL 的下落速度应小于 H 单独的速度 8。",
    title="Tied-Ball Drag Argument",
)

hyp_mass = claim(
    "在亚里士多德定律下，复合体 HL 的总重量大于 H 单独的重量，"
    "因此按该定律，HL 的下落速度应大于 H 单独的速度 8。",
    title="Tied-Ball Mass Argument",
)

hyp_aristotle_vac = claim(
    "若物体下落速度与重量成正比是普遍规律，则在真空中也应如此："
    "较重物体在真空中仍比较轻物体下落更快。",
    title="Aristotle in Vacuum",
)

# W₃ predictions — V 预测斜面实验结果
pred_theta1 = claim(
    "等速假说预测：在近似无摩擦的斜面上（倾角 θ₁），"
    "不同重量的球应呈等加速，距离 ∝ 时间²，与重量无关。",
    title="Plane Prediction θ₁",
)

pred_theta2 = claim(
    "等速假说预测：在另一倾角（θ₂）的斜面上，"
    "同样应呈等加速，距离 ∝ 时间²，与重量无关。",
    title="Plane Prediction θ₂",
)

# ═══════════════════════════════════════════════════════════════════════
# Aristotle branch
# ═══════════════════════════════════════════════════════════════════════

# W₁: 日常观测 → 亚里士多德定律（abduction）
_w1 = abduction(
    obs_daily, hyp_aristotle,
    reason=(
        "日常经验中（@obs_daily），重的石头比轻的羽毛下落更快，"
        "铁球比木球更快。由此推断普遍规律：物体下落速度与重量成正比"
        "（@hyp_aristotle）。"
    ),
)

# A → T₁: 连球拖拽论证（deduction）
deduction(
    [hyp_aristotle], hyp_drag,
    reason=(
        "假设亚里士多德定律（@hyp_aristotle）成立：重物下落更快。"
        "将重球 H（速度 8）与轻球 L（速度 4）绑在一起，"
        "由于 L 比 H 慢，L 会拖拽 H 使复合体减速，"
        "因此复合体 HL 的速度应小于 H 的速度 8（@hyp_drag）。"
    ),
)

# A → T₂: 连球总重论证（deduction）
deduction(
    [hyp_aristotle], hyp_mass,
    reason=(
        "假设亚里士多德定律（@hyp_aristotle）成立：速度与重量成正比。"
        "复合体 HL 的总重量 = H + L > H，按该定律，"
        "HL 的速度应大于 H 的速度 8（@hyp_mass）。"
    ),
)

# T₁ ⊗ T₂: 连球悖论
tied_ball_contradiction = contradiction(
    hyp_drag, hyp_mass,
    reason=(
        "同一复合体 HL 不能同时比 H 慢（@hyp_drag）又比 H 快（@hyp_mass），"
        "这是逻辑矛盾。伽利略原文：'the heavier body moves with less speed "
        "than the lighter; an effect which is contrary to your supposition.'"
    ),
)

# A + S_vac → A_vac: 亚里士多德定律应用于真空（noisy_and）
# 用 noisy_and 而非 deduction：A_vac 的真值因果依赖于 A，
# 当 A 为假时 A_vac 应被拉低（deduction 的 implication 不约束）。
_a_to_avac = noisy_and(
    [hyp_aristotle], hyp_aristotle_vac,
    background=[vacuum],
    reason=(
        "若亚里士多德定律（@hyp_aristotle）是关于下落速度的普遍规律，"
        "将其应用到真空环境（@vacuum）也应成立：在真空中重的物体"
        "仍比轻的下落更快（@hyp_aristotle_vac）。"
    ),
)

# ═══════════════════════════════════════════════════════════════════════
# Galileo branch
# ═══════════════════════════════════════════════════════════════════════

# W₂a: 介质观测 + 空气实验 → 空气阻力假说（induction wrapping abductions）
_w2a = induction(
    [obs_media, obs_air], hyp_air_resistance,
    reason=(
        "在不同介质中（@obs_media），介质越稠密速度差异越大、越稀薄差异越小；"
        "在空气中（@obs_air），重材料球从 100 腕尺落下速度几乎相同。"
        "伽利略由此推断：速度差异完全由介质阻力造成——"
        "阻力是差异的唯一原因（@hyp_air_resistance）。"
        "此推理为溯因推断：不仅编码了'密度越低差异越小'的相关性，"
        "还主张因果机制——阻力决定差异。"
    ),
)

# W₂b: G + S_vac → V（noisy_and）
# 同理：V 的真值因果依赖于 G，当 G 变化时 V 应跟随。
_w2b = noisy_and(
    [hyp_air_resistance], hyp_vacuum_equal,
    background=[vacuum],
    reason=(
        "若阻力是速度差异的唯一原因（@hyp_air_resistance），"
        "且真空中阻力为零（@vacuum），则真空中速度差异为零，"
        "即不同重量物体等速下落（@hyp_vacuum_equal）。"
    ),
)

# ═══════════════════════════════════════════════════════════════════════
# W₃: 斜面实验 — V → predictions ≡ observations
# ═══════════════════════════════════════════════════════════════════════

# V + inclined_plane → predictions（deduction）
deduction(
    [hyp_vacuum_equal], pred_theta1,
    background=[inclined_plane],
    reason=(
        "若真空中不同重量物体等速下落（@hyp_vacuum_equal），"
        "在近似无摩擦的斜面上（@inclined_plane），"
        "不同重量的球也应呈等加速（@pred_theta1）。"
    ),
)

deduction(
    [hyp_vacuum_equal], pred_theta2,
    background=[inclined_plane],
    reason=(
        "若真空中不同重量物体等速下落（@hyp_vacuum_equal），"
        "在另一倾角的斜面上（@inclined_plane），"
        "同样应呈等加速（@pred_theta2）。"
    ),
)

# predictions ≡ observations
equivalence(pred_theta1, obs_theta1,
            reason="第一组斜面预测（@pred_theta1）与观测（@obs_theta1）一致。")

equivalence(pred_theta2, obs_theta2,
            reason="第二组斜面预测（@pred_theta2）与观测（@obs_theta2）一致。")

# ═══════════════════════════════════════════════════════════════════════
# Final contradiction — Aristotle vs Galileo in vacuum
# ═══════════════════════════════════════════════════════════════════════

final_contradiction = contradiction(
    hyp_aristotle_vac, hyp_vacuum_equal,
    reason=(
        "'真空中重者更快'（@hyp_aristotle_vac）与"
        "'真空中等速下落'（@hyp_vacuum_equal）互斥，不能同时为真。"
    ),
)

# ═══════════════════════════════════════════════════════════════════════
# Exported conclusions — cross-package interface
# ═══════════════════════════════════════════════════════════════════════

__all__ = [
    "hyp_air_resistance",
    "hyp_vacuum_equal",
]
