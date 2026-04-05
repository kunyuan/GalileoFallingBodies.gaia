"""Self-review: prior and conditional probability assignments."""

from gaia.review import ReviewBundle, review_claim, review_generated_claim, review_strategy

from .. import (
    hyp_air_resistance,
    hyp_aristotle,
    hyp_aristotle_vac,
    hyp_drag,
    hyp_mass,
    hyp_plane1,
    hyp_plane2,
    hyp_vacuum_equal,
    obs_air,
    obs_daily,
    obs_media,
    obs_theta1,
    obs_theta2,
)

# Strategies that need conditional probabilities
from .. import (
    hyp_aristotle_vac as _hav,
    hyp_plane1 as _hp1,
    hyp_plane2 as _hp2,
    hyp_vacuum_equal as _hve,
)

REVIEW = ReviewBundle(
    source_id="self_review",
    objects=[
        # ── Observation priors ──
        review_claim(obs_daily, prior=0.90,
                     justification="Common everyday experience, highly reliable."),
        review_claim(obs_media, prior=0.90,
                     justification="Well-documented experimental observation."),
        review_claim(obs_air, prior=0.90,
                     justification="Careful experiment in controlled conditions."),
        review_claim(obs_theta1, prior=0.90,
                     justification="Controlled inclined plane experiment."),
        review_claim(obs_theta2, prior=0.90,
                     justification="Repeated experiment at different angle."),

        # ── Hypothesis priors (derived, but validator needs them) ──
        review_claim(hyp_aristotle, prior=0.50,
                     justification="Central hypothesis under test; MaxEnt prior."),
        review_claim(hyp_drag, prior=0.50,
                     justification="Derived from Aristotle; deduction determines belief."),
        review_claim(hyp_mass, prior=0.50,
                     justification="Derived from Aristotle; deduction determines belief."),
        review_claim(hyp_aristotle_vac, prior=0.50,
                     justification="Derived; deduction from Aristotle + vacuum."),
        review_claim(hyp_air_resistance, prior=0.50,
                     justification="Central competing hypothesis; MaxEnt prior."),
        review_claim(hyp_vacuum_equal, prior=0.50,
                     justification="Key conclusion under test."),
        review_claim(hyp_plane1, prior=0.50,
                     justification="Derived from observation + setting."),
        review_claim(hyp_plane2, prior=0.50,
                     justification="Derived from observation + setting."),

        # ── Strategy conditional probabilities ──
        review_strategy(_hav.strategy, conditional_probability=0.90,
                        justification="Direct application of Aristotle's law to vacuum."),
        review_strategy(_hp1.strategy, conditional_probability=0.85,
                        justification="Inclined plane supports equal speed with some uncertainty."),
        review_strategy(_hp2.strategy, conditional_probability=0.85,
                        justification="Second angle confirms with similar reliability."),
        review_strategy(_hve.strategy, conditional_probability=0.90,
                        justification="Air resistance removal logically implies equal speed."),

        # ── Generated alternative_explanation priors ──
        # Abduction: obs_daily → hyp_aristotle
        review_generated_claim(
            hyp_aristotle.strategy, "alternative_explanation",
            prior=0.40,
            justification="Daily observation could be explained by air resistance alone, "
            "not by Aristotle's law. Moderate alternative plausibility.",
        ),
        # Induction sub-abductions: obs_media → hyp_air_resistance
        review_generated_claim(
            hyp_air_resistance.strategy.sub_strategies[0], "alternative_explanation",
            prior=0.20,
            justification="Media observation is hard to explain without air resistance.",
        ),
        # Induction sub-abductions: obs_air → hyp_air_resistance
        review_generated_claim(
            hyp_air_resistance.strategy.sub_strategies[1], "alternative_explanation",
            prior=0.20,
            justification="Controlled air experiment is hard to explain without air resistance.",
        ),
    ],
)
