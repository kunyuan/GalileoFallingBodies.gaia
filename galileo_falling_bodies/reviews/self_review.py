"""Agent-authored review sidecar for the Galileo falling bodies package."""

from gaia.review import ReviewBundle, review_claim, review_strategy

from .. import (
    air_resistance,
    air_resistance_support,
    composite_faster,
    composite_slower,
    heavy_falls_faster,
    vacuum_prediction,
    vacuum_prediction_support,
)

REVIEW = ReviewBundle(
    source_id="galileo_self_review",
    model="agent-authored",
    policy="manual-self-review-v1",
    objects=[
        review_claim(
            heavy_falls_faster,
            prior=0.72,
            judgment="confounded_observation",
            justification=(
                "The observation is real in ordinary air, but it is confounded by drag and "
                "therefore does not directly support an Aristotelian mass law."
            ),
        ),
        review_claim(
            composite_slower,
            prior=0.83,
            judgment="strong_counterfactual_step",
            justification=(
                "Given the Aristotelian premise, attaching a lighter body predicts a drag-like "
                "effect that should slow the heavier body."
            ),
        ),
        review_claim(
            composite_faster,
            prior=0.91,
            judgment="strong_counterfactual_step",
            justification=(
                "Under the same doctrine, the tied composite has greater total mass and should "
                "therefore fall faster."
            ),
        ),
        review_claim(
            air_resistance,
            prior=0.84,
            judgment="well_supported_explanation",
            justification=(
                "The contradiction in the Aristotelian model strongly supports the interpretation "
                "that ordinary observed speed differences arise from drag."
            ),
        ),
        review_claim(
            vacuum_prediction,
            prior=0.88,
            judgment="strong_conclusion",
            justification=(
                "Once drag is removed as the confounder, the remaining explanation predicts equal "
                "free-fall acceleration across masses."
            ),
        ),
        review_strategy(
            air_resistance_support,
            conditional_probability=0.92,
            judgment="highly_reliable_support",
            justification=(
                "If the tied-ball contradiction is accepted, it very strongly supports the drag "
                "explanation for ordinary observations."
            ),
        ),
        review_strategy(
            vacuum_prediction_support,
            conditional_probability=0.89,
            judgment="strong_support",
            justification=(
                "The contradiction plus the empirical observation of apparent mass differences "
                "jointly provide strong support for the vacuum prediction."
            ),
        ),
    ],
)
