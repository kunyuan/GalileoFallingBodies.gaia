"""Galileo's falling bodies argument — Gaia knowledge package."""

from gaia.lang import claim, contradiction, setting

# ── Background ──
aristotle_doctrine = setting("""
    Aristotle's doctrine: heavier objects fall proportionally faster.
""")
aristotle_doctrine.label = "aristotle_doctrine"

# ── Observations ──
heavy_falls_faster = claim(r"""
    Observations show heavier stones fall faster than feathers.
""")
heavy_falls_faster.label = "heavy_falls_faster"

# ── Thought experiment ──
composite_slower = claim(r"""
    The tied composite should be slower (light ball drags heavy ball).
    $v_{\text{composite}} = \frac{m_1 v_1 + m_2 v_2}{m_1 + m_2}$
""")
composite_slower.label = "composite_slower"

composite_faster = claim(r"""
    The composite has greater mass, so it should be faster.
    $v_{\text{composite}} = k(m_1 + m_2) > k m_1$
""")
composite_faster.label = "composite_faster"

# ── Contradiction ──
tied_ball = contradiction(
    composite_slower,
    composite_faster,
    reason="Same premise yields contradictory conclusions",
)
tied_ball.label = "tied_ball"

# ── Conclusions ──
air_resistance = claim(
    """
    Observed speed differences are caused entirely by air resistance.
""",
    given=[tied_ball],
)
air_resistance_support = air_resistance.strategy

vacuum_prediction = claim(
    r"""
    In a vacuum, objects of different mass fall at the same rate.
    $g \approx 9.8 \text{ m/s}^2$, independent of mass.
""",
    given=[tied_ball, heavy_falls_faster],
)
vacuum_prediction_support = vacuum_prediction.strategy

__all__ = [
    "aristotle_doctrine",
    "heavy_falls_faster",
    "composite_slower",
    "composite_faster",
    "tied_ball",
    "air_resistance",
    "vacuum_prediction",
]
