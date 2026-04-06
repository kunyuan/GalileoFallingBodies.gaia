"""Self-review: prior and conditional probability assignments."""

from gaia.review import ReviewBundle, review_claim, review_generated_claim, review_strategy

from .. import (
    hyp_air_resistance,
    hyp_aristotle,
    hyp_aristotle_vac,
    hyp_drag,
    hyp_mass,
    hyp_vacuum_equal,
    obs_air,
    obs_daily,
    obs_media,
    obs_theta1,
    obs_theta2,
    pred_theta1,
    pred_theta2,
)

# Strategies that need conditional probabilities
from .. import _a_to_avac, _w2b

# W₁ abduction strategy — need to reference for generated alt claim
from .. import _w1

# W₂a induction strategy — sub-abductions for generated alt claims
from .. import _w2a

REVIEW = ReviewBundle(
    source_id="self_review",
    objects=[
        # ── Observation priors ──
        review_claim(obs_daily, prior=0.90,
                     justification="Common everyday experience, highly reliable."),
        review_claim(obs_media, prior=0.90,
                     justification="Well-documented experimental observation across media."),
        review_claim(obs_air, prior=0.90,
                     justification="Careful experiment with heavy materials, small residual."),
        review_claim(obs_theta1, prior=0.90,
                     justification="Controlled inclined plane experiment."),
        review_claim(obs_theta2, prior=0.90,
                     justification="Repeated experiment at different angle, 100 repetitions."),

        # ── Hypothesis priors (derived, but validator needs them) ──
        review_claim(hyp_aristotle, prior=0.50,
                     justification="Central hypothesis under test; MaxEnt prior."),
        review_claim(hyp_air_resistance, prior=0.50,
                     justification="Central competing hypothesis; MaxEnt prior."),
        review_claim(hyp_vacuum_equal, prior=0.50,
                     justification="Key conclusion under test; belief from BP."),
        review_claim(hyp_drag, prior=0.50,
                     justification="Derived from Aristotle; deduction determines belief."),
        review_claim(hyp_mass, prior=0.50,
                     justification="Derived from Aristotle; deduction determines belief."),
        review_claim(hyp_aristotle_vac, prior=0.50,
                     justification="Derived; deduction from Aristotle + vacuum."),
        review_claim(pred_theta1, prior=0.50,
                     justification="Derived; deduction from vacuum equal speed."),
        review_claim(pred_theta2, prior=0.50,
                     justification="Derived; deduction from vacuum equal speed."),

        # ── Strategy conditional probabilities (noisy_and) ──
        review_strategy(_a_to_avac, conditional_probability=0.95,
                        justification="Near-deterministic: universal law applied to vacuum."),
        review_strategy(_w2b, conditional_probability=0.95,
                        justification="Near-deterministic: sole cause removed → effect vanishes."),

        # ── Generated alternative_explanation priors ──
        # W₁ abduction: obs_daily → hyp_aristotle
        # π(Alt) = "can Alt alone explain obs_daily without Aristotle?"
        # Yes, air resistance alone can explain why heavy things fall faster
        # in daily life — moderate alternative plausibility.
        review_generated_claim(
            _w1, "alternative_explanation",
            prior=0.40,
            justification="Daily observation could be explained by air resistance alone, "
            "not by Aristotle's law. Moderate alternative plausibility.",
        ),

        # W₂a induction sub-abductions: obs_media → hyp_air_resistance
        # π(Alt) = "can Alt explain obs_media without air resistance hypothesis?"
        # Hard — the systematic pattern across media densities strongly points
        # to resistance as the cause.
        review_generated_claim(
            _w2a.sub_strategies[0], "alternative_explanation",
            prior=0.20,
            justification="Media density pattern is hard to explain without "
            "air resistance as the causal mechanism.",
        ),

        # W₂a induction sub-abductions: obs_air → hyp_air_resistance
        review_generated_claim(
            _w2a.sub_strategies[1], "alternative_explanation",
            prior=0.20,
            justification="Near-equal fall times for heavy materials in air "
            "is hard to explain without air resistance hypothesis.",
        ),
    ],
)
