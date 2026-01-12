#!/usr/bin/env python3
"""
Batch 3 Parallel Research Orchestrator
50機関を10エージェントで並列調査
"""

# エージェント割り当て定義
AGENT_ASSIGNMENTS = {
    "agent_01": [
        "1101_東京大学",
        "1102_京都大学", 
        "1103_大阪大学",
        "1104_東北大学",
        "1105_名古屋大学"
    ],
    "agent_02": [
        "1106_九州大学",
        "1107_北海道大学",
        "1108_東京工業大学",
        "1109_筑波大学",
        "1110_神戸大学"
    ],
    "agent_03": [
        "1111_広島大学",
        "1112_千葉大学",
        "1113_金沢大学",
        "1114_岡山大学",
        "1115_熊本大学"
    ],
    "agent_04": [
        "1116_新潟大学",
        "1117_長崎大学",
        "1118_鹿児島大学",
        "1119_信州大学",
        "1120_群馬大学"
    ],
    "agent_05": [
        "1121_早稲田大学",
        "1122_慶應義塾大学",
        "1123_上智大学",
        "1124_明治大学",
        "1125_立教大学"
    ],
    "agent_06": [
        "1126_中央大学",
        "1127_法政大学",
        "1128_青山学院大学",
        "1129_学習院大学",
        "1130_東京理科大学"
    ],
    "agent_07": [
        "1131_同志社大学",
        "1132_立命館大学",
        "1133_関西大学",
        "1134_関西学院大学",
        "1135_近畿大学"
    ],
    "agent_08": [
        "1136_龍谷大学",
        "1137_甲南大学",
        "1138_京都産業大学",
        "1139_南山大学",
        "1140_理化学研究所"
    ],
    "agent_09": [
        "1141_産業技術総合研究所",
        "1142_物質・材料研究機構",
        "1143_宇宙航空研究開発機構JAXA",
        "1144_海洋研究開発機構JAMSTEC",
        "1145_農業・食品産業技術総合研究機構"
    ],
    "agent_10": [
        "1146_国立がん研究センター",
        "1147_国立循環器病研究センター",
        "1148_国立精神・神経医療研究センター",
        "1149_情報通信研究機構NICT",
        "1150_防災科学技術研究所"
    ]
}

OUTPUT_DIR = "/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-08/university_research_batch3"

print("=== Batch 3 Parallel Research Orchestrator ===")
print(f"Total institutions: 50")
print(f"Parallel agents: 10")
print(f"Institutions per agent: 5")
print(f"Output directory: {OUTPUT_DIR}")
print("\nAgent assignments:")
for agent_id, institutions in AGENT_ASSIGNMENTS.items():
    print(f"\n{agent_id}:")
    for inst in institutions:
        print(f"  - {inst}")

print("\n=== Ready for parallel execution ===")
print("Use Claude Code Task tool to launch 10 parallel subagents")
