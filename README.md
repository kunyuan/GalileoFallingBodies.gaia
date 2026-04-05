# galileo-falling-bodies-gaia

Galileo's falling bodies argument — Gaia knowledge package

## Overview

```mermaid
graph LR
    aristotle_doctrine["aristotle_doctrine"]:::setting
    heavy_falls_faster["heavy_falls_faster"]:::premise
    composite_slower["composite_slower"]:::premise
    composite_faster["composite_faster"]:::premise
    tied_ball["tied_ball"]:::derived
    air_resistance["air_resistance"]:::derived
    vacuum_prediction["vacuum_prediction"]:::derived
    composite_faster --> tied_ball
    composite_slower --> tied_ball
    heavy_falls_faster --> vacuum_prediction
    tied_ball --> air_resistance
    tied_ball --> vacuum_prediction

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

## Introduction

#### aristotle_doctrine ★

📋 `aristotle_doctrine`

> Aristotle's doctrine: heavier objects fall proportionally faster.


#### heavy_falls_faster ★

📌 `heavy_falls_faster`

> Observations show heavier stones fall faster than feathers.


#### composite_slower ★

📌 `composite_slower`

> The tied composite should be slower (light ball drags heavy ball).
>     $v_{\text{composite}} = \frac{m_1 v_1 + m_2 v_2}{m_1 + m_2}$


#### composite_faster ★

📌 `composite_faster`

> The composite has greater mass, so it should be faster.
>     $v_{\text{composite}} = k(m_1 + m_2) > k m_1$


#### tied_ball ★

📌 `tied_ball`

> not_both_true(composite_slower, composite_faster)


#### air_resistance ★

📌 `air_resistance`

> Observed speed differences are caused entirely by air resistance.

🔗 **noisy_and**([tied_ball](#tied_ball))


#### vacuum_prediction ★

📌 `vacuum_prediction`

> In a vacuum, objects of different mass fall at the same rate.
>     $g \approx 9.8 \text{ m/s}^2$, independent of mass.

🔗 **noisy_and**([tied_ball](#tied_ball), [heavy_falls_faster](#heavy_falls_faster))



## Knowledge Graph

```mermaid
graph TD
    aristotle_doctrine["aristotle_doctrine"]:::setting
    heavy_falls_faster["heavy_falls_faster"]:::premise
    composite_slower["composite_slower"]:::premise
    composite_faster["composite_faster"]:::premise
    tied_ball["tied_ball"]:::derived
    air_resistance["air_resistance"]:::derived
    vacuum_prediction["vacuum_prediction"]:::derived
    strat_0(["noisy_and"]):::weak
    tied_ball --> strat_0
    strat_0 --> air_resistance
    strat_1(["noisy_and"]):::weak
    tied_ball --> strat_1
    heavy_falls_faster --> strat_1
    strat_1 --> vacuum_prediction
    oper_0{{"⊗"}}:::contra
    composite_slower --- oper_0
    composite_faster --- oper_0
    oper_0 --- tied_ball

    classDef setting fill:#f0f0f0,stroke:#999,color:#333
    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef derived fill:#ddffdd,stroke:#44bb44,color:#333
    classDef question fill:#fff3dd,stroke:#cc9944,color:#333
    classDef background fill:#f5f5f5,stroke:#bbb,stroke-dasharray: 5 5,color:#333
    classDef orphan fill:#fff,stroke:#ccc,stroke-dasharray: 5 5,color:#333
    classDef external fill:#fff,stroke:#aaa,stroke-dasharray: 3 3,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

## Knowledge Nodes

### Settings

<a id="aristotle_doctrine"></a>

#### aristotle_doctrine ★

📋 `aristotle_doctrine`

> Aristotle's doctrine: heavier objects fall proportionally faster.


### Claims

<a id="composite_faster"></a>

#### composite_faster ★

📌 `composite_faster`

> The composite has greater mass, so it should be faster.
>     $v_{\text{composite}} = k(m_1 + m_2) > k m_1$


<a id="composite_slower"></a>

#### composite_slower ★

📌 `composite_slower`

> The tied composite should be slower (light ball drags heavy ball).
>     $v_{\text{composite}} = \frac{m_1 v_1 + m_2 v_2}{m_1 + m_2}$


<a id="heavy_falls_faster"></a>

#### heavy_falls_faster ★

📌 `heavy_falls_faster`

> Observations show heavier stones fall faster than feathers.


<a id="tied_ball"></a>

#### tied_ball ★

📌 `tied_ball`

> not_both_true(composite_slower, composite_faster)


<a id="air_resistance"></a>

#### air_resistance ★

📌 `air_resistance`

> Observed speed differences are caused entirely by air resistance.

🔗 **noisy_and**([tied_ball](#tied_ball))


<a id="vacuum_prediction"></a>

#### vacuum_prediction ★

📌 `vacuum_prediction`

> In a vacuum, objects of different mass fall at the same rate.
>     $g \approx 9.8 \text{ m/s}^2$, independent of mass.

🔗 **noisy_and**([tied_ball](#tied_ball), [heavy_falls_faster](#heavy_falls_faster))

