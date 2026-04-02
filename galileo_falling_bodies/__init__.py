"""Galileo's falling bodies argument — Gaia knowledge package."""

from gaia.lang import Package, claim, contradiction, setting

with Package("galileo_falling_bodies", namespace="reg", version="4.0.3") as pkg:

    # ── Background ──
    aristotle_doctrine = setting("""
        Aristotle's doctrine: heavier objects fall proportionally faster.
    """)

    # ── Observations ──
    heavy_falls_faster = claim(r"""
        Observations show heavier stones fall faster than feathers.
    """)

    # ── Thought experiment ──
    composite_slower = claim(r"""
        The tied composite should be slower (light ball drags heavy ball).
        $v_{\text{composite}} = \frac{m_1 v_1 + m_2 v_2}{m_1 + m_2}$
    """)

    composite_faster = claim(r"""
        The composite has greater mass, so it should be faster.
        $v_{\text{composite}} = k(m_1 + m_2) > k m_1$
    """)

    # ── Contradiction ──
    tied_ball = contradiction(
        composite_slower, composite_faster,
        reason="Same premise yields contradictory conclusions",
    )

    # ── Conclusions ──
    air_resistance = claim("""
        Observed speed differences are caused entirely by air resistance.
    """, given=[tied_ball])

    vacuum_prediction = claim(r"""
        In a vacuum, objects of different mass fall at the same rate.
        $g \approx 9.8 \text{ m/s}^2$, independent of mass.
    """, given=[tied_ball, heavy_falls_faster])

__all__ = ["vacuum_prediction", "air_resistance"]
