# galileo-falling-bodies-gaia

Galileo's falling bodies argument — Gaia knowledge package

## Overview

```mermaid
graph LR
    hyp_air_resistance["Air Resistance Hypothesis"]:::derived
    hyp_vacuum_equal["Vacuum Equal Speed"]:::derived
    hyp_air_resistance --> hyp_vacuum_equal

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

#### Air Resistance Hypothesis ★

📌 `hyp_air_resistance`

> 日常观察到的速度差异由空气阻力造成，而非重量本身决定。

🔗 **induction**([Media Observation](#obs_media), [Air Experiment](#obs_air))


#### Vacuum Equal Speed ★

📌 `hyp_vacuum_equal`

> 如果速度差异纯由空气阻力造成，则在真空中不同重量物体应等速下落。

🔗 **noisy_and**([Air Resistance Hypothesis](#hyp_air_resistance))



## Knowledge Graph

```mermaid
graph TD
    vacuum["vacuum"]:::setting
    inclined_plane["inclined_plane"]:::setting
    obs_daily["Daily Observation"]:::premise
    obs_media["Media Observation"]:::premise
    obs_air["Air Experiment"]:::premise
    obs_theta1["Inclined Plane 30°"]:::premise
    obs_theta2["Inclined Plane 60°"]:::premise
    hyp_aristotle["Aristotle's Law"]:::derived
    pred_daily["Aristotle Daily Prediction"]:::derived
    [""]:::derived
    hyp_drag["Drag Argument (T1)"]:::derived
    hyp_mass["Mass Argument (T2)"]:::derived
    tied_ball_contradiction["tied_ball_contradiction"]:::derived
    hyp_aristotle_vac["Aristotle in Vacuum"]:::derived
    hyp_air_resistance["Air Resistance Hypothesis"]:::derived
    pred_media["Media Prediction"]:::derived
    [""]:::derived
    pred_air["Air Prediction"]:::derived
    [""]:::derived
    hyp_vacuum_equal["Vacuum Equal Speed"]:::derived
    hyp_plane1["Plane Evidence 1"]:::derived
    hyp_plane2["Plane Evidence 2"]:::derived
    pred_theta1["Plane Prediction 1"]:::derived
    [""]:::derived
    pred_theta2["Plane Prediction 2"]:::derived
    [""]:::derived
    final_contradiction["final_contradiction"]:::derived
    strat_0(["abduction"]):::weak
    obs_daily --> strat_0
    strat_0 --> hyp_aristotle
    strat_1(["deduction"])
    hyp_aristotle --> strat_1
    strat_1 --> pred_daily
    strat_2(["deduction"])
    hyp_aristotle --> strat_2
    strat_2 --> hyp_drag
    strat_3(["deduction"])
    hyp_aristotle --> strat_3
    strat_3 --> hyp_mass
    strat_4(["noisy_and"]):::weak
    hyp_aristotle --> strat_4
    vacuum -.-> strat_4
    strat_4 --> hyp_aristotle_vac
    strat_5(["abduction"]):::weak
    obs_media --> strat_5
    strat_5 --> hyp_air_resistance
    strat_6(["abduction"]):::weak
    obs_air --> strat_6
    strat_6 --> hyp_air_resistance
    strat_7(["induction"]):::weak
    obs_media --> strat_7
    obs_air --> strat_7
    strat_7 --> hyp_air_resistance
    strat_8(["deduction"])
    hyp_air_resistance --> strat_8
    strat_8 --> pred_media
    strat_9(["deduction"])
    hyp_air_resistance --> strat_9
    strat_9 --> pred_air
    strat_10(["noisy_and"]):::weak
    hyp_air_resistance --> strat_10
    vacuum -.-> strat_10
    strat_10 --> hyp_vacuum_equal
    strat_11(["noisy_and"]):::weak
    obs_theta1 --> strat_11
    inclined_plane -.-> strat_11
    strat_11 --> hyp_plane1
    strat_12(["noisy_and"]):::weak
    obs_theta2 --> strat_12
    inclined_plane -.-> strat_12
    strat_12 --> hyp_plane2
    strat_13(["deduction"])
    hyp_plane1 --> strat_13
    strat_13 --> pred_theta1
    strat_14(["deduction"])
    hyp_plane2 --> strat_14
    strat_14 --> pred_theta2
    oper_0{{"≡"}}
    pred_daily --- oper_0
    obs_daily --- oper_0
    oper_0 --- 
    oper_1{{"⊗"}}:::contra
    hyp_drag --- oper_1
    hyp_mass --- oper_1
    oper_1 --- tied_ball_contradiction
    oper_2{{"≡"}}
    pred_media --- oper_2
    obs_media --- oper_2
    oper_2 --- 
    oper_3{{"≡"}}
    pred_air --- oper_3
    obs_air --- oper_3
    oper_3 --- 
    oper_4{{"≡"}}
    pred_theta1 --- oper_4
    obs_theta1 --- oper_4
    oper_4 --- 
    oper_5{{"≡"}}
    pred_theta2 --- oper_5
    obs_theta2 --- oper_5
    oper_5 --- 
    oper_6{{"⊗"}}:::contra
    hyp_aristotle_vac --- oper_6
    hyp_vacuum_equal --- oper_6
    oper_6 --- final_contradiction

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

<a id="inclined_plane"></a>

#### inclined_plane

📋 `inclined_plane`

> 伽利略斜面实验的精确受控环境。


<a id="vacuum"></a>

#### vacuum

📋 `vacuum`

> 理想化的无空气阻力真空环境，只保留重力作用。


### Claims

<a id="obs_air"></a>

#### Air Experiment

📌 `obs_air`

> 在空气中做精细实验，重量差异较大的物体几乎同时落地，轻微差异可归因于空气阻力。


<a id="obs_daily"></a>

#### Daily Observation

📌 `obs_daily`

> 日常经验中，重的石头确实比轻的羽毛下落得快。


<a id="obs_media"></a>

#### Media Observation

📌 `obs_media`

> 在水、油等不同介质中比较轻重物体下落，介质越稠密速度差异越大，越稀薄差异越小。


<a id="obs_theta1"></a>

#### Inclined Plane 30°

📌 `obs_theta1`

> 斜面实验第一组：不同重量小球在 30° 斜面呈现近似一致加速趋势。


<a id="obs_theta2"></a>

#### Inclined Plane 60°

📌 `obs_theta2`

> 斜面实验第二组：60° 斜面重复实验，结果一致确认等加速。


<a id="hyp_air_resistance"></a>

#### Air Resistance Hypothesis ★

📌 `hyp_air_resistance`

> 日常观察到的速度差异由空气阻力造成，而非重量本身决定。

🔗 **induction**([Media Observation](#obs_media), [Air Experiment](#obs_air))


<a id="hyp_aristotle"></a>

#### Aristotle's Law

📌 `hyp_aristotle`

> 物体下落速度与重量成正比：重物比轻物下落更快。

🔗 **abduction**([Daily Observation](#obs_daily))


<a id="hyp_plane1"></a>

#### Plane Evidence 1

📌 `hyp_plane1`

> 第一组斜面实验支持真空等速下落。

🔗 **noisy_and**([Inclined Plane 30°](#obs_theta1))


<a id="hyp_plane2"></a>

#### Plane Evidence 2

📌 `hyp_plane2`

> 第二组斜面实验支持真空等速下落。

🔗 **noisy_and**([Inclined Plane 60°](#obs_theta2))


<a id="hyp_aristotle_vac"></a>

#### Aristotle in Vacuum

📌 `hyp_aristotle_vac`

> 按亚里士多德定律，在真空中也应重者下落更快。

🔗 **noisy_and**([Aristotle's Law](#hyp_aristotle))


<a id="hyp_drag"></a>

#### Drag Argument (T1)

📌 `hyp_drag`

> 假设重物下落更快，将重球 H 与轻球 L 绑在一起，L 拖拽 H，复合体 HL 速度应慢于 H 单独下落。

🔗 **deduction**([Aristotle's Law](#hyp_aristotle))


<a id="hyp_mass"></a>

#### Mass Argument (T2)

📌 `hyp_mass`

> 假设重物下落更快，复合体 HL 总重量大于 H，因此 HL 速度应快于 H 单独下落。

🔗 **deduction**([Aristotle's Law](#hyp_aristotle))


<a id="hyp_vacuum_equal"></a>

#### Vacuum Equal Speed ★

📌 `hyp_vacuum_equal`

> 如果速度差异纯由空气阻力造成，则在真空中不同重量物体应等速下落。

🔗 **noisy_and**([Air Resistance Hypothesis](#hyp_air_resistance))


<a id="pred_air"></a>

#### Air Prediction

📌 `pred_air`

> 空气阻力假说预测：在空气中做精细实验，应观测到轻重物体几乎同速。

🔗 **deduction**([Air Resistance Hypothesis](#hyp_air_resistance))


<a id="pred_daily"></a>

#### Aristotle Daily Prediction

📌 `pred_daily`

> 亚里士多德定律预测：日常中重物应比轻物下落更快。

🔗 **deduction**([Aristotle's Law](#hyp_aristotle))


<a id="pred_media"></a>

#### Media Prediction

📌 `pred_media`

> 空气阻力假说预测：在不同密度介质中，密度越低则轻重物体速度差越小。

🔗 **deduction**([Air Resistance Hypothesis](#hyp_air_resistance))


<a id="pred_theta1"></a>

#### Plane Prediction 1

📌 `pred_theta1`

> 等速假说预测第一组斜面实验应呈等加速。

🔗 **deduction**([Plane Evidence 1](#hyp_plane1))


<a id="pred_theta2"></a>

#### Plane Prediction 2

📌 `pred_theta2`

> 等速假说预测第二组斜面实验应呈等加速。

🔗 **deduction**([Plane Evidence 2](#hyp_plane2))


#### 

📌 ``

> same_truth(A, B)


#### 

📌 ``

> same_truth(A, B)


#### 

📌 ``

> same_truth(A, B)


#### 

📌 ``

> same_truth(A, B)


#### 

📌 ``

> same_truth(A, B)


<a id="final_contradiction"></a>

#### final_contradiction

📌 `final_contradiction`

> not_both_true(A, B)


<a id="tied_ball_contradiction"></a>

#### tied_ball_contradiction

📌 `tied_ball_contradiction`

> not_both_true(A, B)


## Inference Results

**BP converged:** True (2 iterations)

| Label | Type | Prior | Belief | Role |
|-------|------|-------|--------|------|
| [composite_slower](#composite_slower) |  | 0.83 | 0.3075 | orphaned |
| [composite_faster](#composite_faster) |  | 0.91 | 0.6334 | orphaned |
| [vacuum_prediction](#vacuum_prediction) |  | 0.88 | 0.9288 | orphaned |
| [heavy_falls_faster](#heavy_falls_faster) |  | 0.72 | 0.9439 | orphaned |
| [air_resistance](#air_resistance) |  | 0.84 | 0.9836 | orphaned |
| [tied_ball](#tied_ball) |  | — | 0.9999 | orphaned |
