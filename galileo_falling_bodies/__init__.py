"""Galileo's Falling Bodies — fine-grained reasoning graph.

Formalizes Galileo's argument against Aristotle's doctrine that heavier
objects fall faster, including the tied-ball thought experiment, the air
resistance hypothesis, and inclined plane experimental evidence.
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

vacuum = setting("理想化的无空气阻力真空环境，只保留重力作用。")
inclined_plane = setting("伽利略斜面实验的精确受控环境。")

# ═══════════════════════════════════════════════════════════════════════
# Observations — empirical evidence (leaf claims, reviewer assigns priors)
# ═══════════════════════════════════════════════════════════════════════

obs_daily = claim(
    "日常经验中，重的石头确实比轻的羽毛下落得快。",
    title="Daily Observation",
)

obs_media = claim(
    "在水、油等不同介质中比较轻重物体下落，"
    "介质越稠密速度差异越大，越稀薄差异越小。",
    title="Media Observation",
)

obs_air = claim(
    "在空气中做精细实验，重量差异较大的物体"
    "几乎同时落地，轻微差异可归因于空气阻力。",
    title="Air Experiment",
)

obs_theta1 = claim(
    "斜面实验第一组：不同重量小球在 30° 斜面呈现近似一致加速趋势。",
    title="Inclined Plane 30°",
)

obs_theta2 = claim(
    "斜面实验第二组：60° 斜面重复实验，结果一致确认等加速。",
    title="Inclined Plane 60°",
)

# ═══════════════════════════════════════════════════════════════════════
# Aristotle branch
# ═══════════════════════════════════════════════════════════════════════

# Daily observation → Aristotle's hypothesis (abduction)
hyp_aristotle = claim(
    "物体下落速度与重量成正比：重物比轻物下落更快。",
    title="Aristotle's Law",
)
abduction(obs_daily, hyp_aristotle)

# Aristotle's law → daily prediction (deduction)
pred_daily = claim(
    "亚里士多德定律预测：日常中重物应比轻物下落更快。",
    title="Aristotle Daily Prediction",
)
deduction([hyp_aristotle], pred_daily)

# Prediction matches observation
equivalence(pred_daily, obs_daily, reason="亚里士多德的日常预测与日常观测一致。")

# Tied-ball thought experiment: two contradictory predictions from A
hyp_drag = claim(
    "假设重物下落更快，将重球 H 与轻球 L 绑在一起，"
    "L 拖拽 H，复合体 HL 速度应慢于 H 单独下落。",
    title="Drag Argument (T1)",
)
deduction([hyp_aristotle], hyp_drag)

hyp_mass = claim(
    "假设重物下落更快，复合体 HL 总重量大于 H，"
    "因此 HL 速度应快于 H 单独下落。",
    title="Mass Argument (T2)",
)
deduction([hyp_aristotle], hyp_mass)

# T1 ⊗ T2: contradiction
tied_ball_contradiction = contradiction(
    hyp_drag, hyp_mass,
    reason="T1 与 T2 互相矛盾：复合体 HL 不能同时慢于 H 又快于 H。",
)

# Aristotle in vacuum
hyp_aristotle_vac = claim(
    "按亚里士多德定律，在真空中也应重者下落更快。",
    title="Aristotle in Vacuum",
)
noisy_and([hyp_aristotle], hyp_aristotle_vac, background=[vacuum])

# ═══════════════════════════════════════════════════════════════════════
# Galileo branch
# ═══════════════════════════════════════════════════════════════════════

# Two observations → air resistance hypothesis (induction)
hyp_air_resistance = claim(
    "日常观察到的速度差异由空气阻力造成，而非重量本身决定。",
    title="Air Resistance Hypothesis",
)
induction([obs_media, obs_air], hyp_air_resistance)

# Air resistance → media prediction (deduction)
pred_media = claim(
    "空气阻力假说预测：在不同密度介质中，密度越低则轻重物体速度差越小。",
    title="Media Prediction",
)
deduction([hyp_air_resistance], pred_media)

equivalence(pred_media, obs_media, reason="介质预测与介质观测一致。")

# Air resistance → air prediction (deduction)
pred_air = claim(
    "空气阻力假说预测：在空气中做精细实验，应观测到轻重物体几乎同速。",
    title="Air Prediction",
)
deduction([hyp_air_resistance], pred_air)

equivalence(pred_air, obs_air, reason="空气预测与空气实验一致。")

# Air resistance + vacuum → equal speed in vacuum
hyp_vacuum_equal = claim(
    "如果速度差异纯由空气阻力造成，则在真空中不同重量物体应等速下落。",
    title="Vacuum Equal Speed",
)
noisy_and([hyp_air_resistance], hyp_vacuum_equal, background=[vacuum])

# ═══════════════════════════════════════════════════════════════════════
# Inclined plane evidence — induction supporting vacuum equal speed
# ═══════════════════════════════════════════════════════════════════════

hyp_plane1 = claim(
    "第一组斜面实验支持真空等速下落。",
    title="Plane Evidence 1",
)
noisy_and([obs_theta1], hyp_plane1, background=[inclined_plane])

hyp_plane2 = claim(
    "第二组斜面实验支持真空等速下落。",
    title="Plane Evidence 2",
)
noisy_and([obs_theta2], hyp_plane2, background=[inclined_plane])

# Predictions from equal-speed hypothesis
pred_theta1 = claim(
    "等速假说预测第一组斜面实验应呈等加速。",
    title="Plane Prediction 1",
)
deduction([hyp_plane1], pred_theta1)

equivalence(pred_theta1, obs_theta1, reason="第一组斜面预测与观测一致。")

pred_theta2 = claim(
    "等速假说预测第二组斜面实验应呈等加速。",
    title="Plane Prediction 2",
)
deduction([hyp_plane2], pred_theta2)

equivalence(pred_theta2, obs_theta2, reason="第二组斜面预测与观测一致。")

# ═══════════════════════════════════════════════════════════════════════
# Final contradiction — Aristotle vs Galileo in vacuum
# ═══════════════════════════════════════════════════════════════════════

final_contradiction = contradiction(
    hyp_aristotle_vac, hyp_vacuum_equal,
    reason="真空中不能同时'重者更快'又'等速下落'。",
)

# ═══════════════════════════════════════════════════════════════════════
# Exported conclusions — cross-package interface
# ═══════════════════════════════════════════════════════════════════════

__all__ = [
    "hyp_air_resistance",
    "hyp_vacuum_equal",
]
