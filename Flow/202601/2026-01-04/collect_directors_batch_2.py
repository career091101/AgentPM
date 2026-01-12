#!/usr/bin/env python3
"""
Collect director names for dental clinics from rows 108-214.
Uses WebFetch for official websites and WebSearch as fallback.
"""

import csv
import json
import time
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# CSV data for rows 108-214
DENTAL_CLINICS = [
    ("むらつ歯科クリニック", "https://muratsu-dc.jp/"),
    ("博多矯正歯科KITTE博多院", "https://www.hakatakyousei.com/"),
    ("Oh my teeth 福岡博多矯正歯科", "https://www.oh-my-teeth.com/locations/hakata/"),
    ("MC天神こが歯科・矯正歯科", "https://mctenjin-kogadental.com/"),
    ("Sagan歯科こども歯科医院", "https://sagan-dental.com/"),
    ("佐賀さくら歯科親子歯科クリニック", "https://sagasakura.com/"),
    ("みらい歯科・こども矯正歯科", "https://www.mirai-dental.com/"),
    ("緒方歯科クリニック", "http://www.ogata-dental.net/"),
    ("イターナル歯科クリニック 佐賀本院", "https://www.eternal-dc.com/"),
    ("佐賀駅前矯正歯科", "https://saga-ortho.com/"),
    ("（医）TERRA寺谷矯正歯科クリニック", "http://www.terra-kyousei.com/"),
    ("スマイル髙城歯科", "https://www.smileshika.net/"),
    ("松尾歯科矯正歯科", "https://www.matsuodc.com/"),
    ("ルアナファミリー歯科・矯正歯科", "https://kiyama-dc.com/"),
    ("田口歯科医院", "http://www.taguchi-kidsdc.com/"),
    ("諫早ふじた歯科・矯正歯科", "https://fujitashika.com/"),
    ("すずき矯正歯科", "http://www.suzuki-or.com/"),
    ("長崎マウスピース矯正歯科", "https://nagasaki-mouthpiece.com/"),
    ("プレミアスマイル長崎矯正歯科", "https://www.premiersmile4u.com/"),
    ("堀内歯科 矯正歯科・小児歯科", "https://www.horiuchi-sika.com/"),
    ("ブライトデンタルクリニック", "https://www.bright-dc.net/"),
    ("初台 はまだ歯科・矯正歯科", "http://www.hamada-dc.com/"),
    ("ひかる歯科ちえこども歯科", "https://hikarushika.com/"),
    ("新屋敷津田歯科こども歯科", "http://www.tsuda-dental.com/"),
    ("熊本パール総合歯科・矯正歯科・こども歯科クリニック 中央院", "http://www.par-dc.jp/"),
    ("いろどり歯科こども歯科クリニック", "https://irodori-kids-dc.com/"),
    ("熊本パール総合歯科・矯正歯科・こども歯科クリニック SAKURA MACHI Kumamoto院", "https://www.par-dc.jp/"),
    ("出口歯科おとな•こども歯科クリニック", "https://www.deguchi-dc.jp/"),
    ("熊本パール総合歯科・矯正歯科・こども歯科クリニック 宇土院", "http://www.par-dc.jp/"),
    ("やまだ歯科・こども歯科・矯正歯科クリニック熊本院", "https://www.yamada-kidsdc.com/"),
    ("熊本パール総合歯科·矯正歯科·こども歯科クリニック 健軍院", "http://www.par-dc.jp/"),
    ("クリア総合歯科クリニック", "https://clear-dc.com/"),
    ("熊本フェリス総合歯科クリニック", "https://feliz-dc.com/"),
    ("ひがし歯科医院", "https://www.higashishika.com/"),
    ("医療法人社団幸歯会 元島歯科クリニック", "https://motoshima-dc.jp/"),
    ("熊本上通矯正歯科クリニック", "https://dd-dentalclinic.jp/lp/ddd/lp01/"),
    ("熊本DAN矯正歯科クリニック", "http://www.dan-kyousei.com/"),
    ("医療法人 熊本駅前矯正歯科クリニック", "https://kumamoto-ekimae-kc.com/"),
    ("けやき通り歯科・矯正歯科", "https://www.keyaki.org/"),
    ("熊本パール総合歯科・矯正歯科クリニックAMUPLAZA熊本院", "https://www.par-dc.jp/"),
    ("川口歯科医院", "http://kumamoto-shika.com/"),
    ("医療法人友枝会 友枝総合歯科・矯正歯科", "https://tdc-kumamoto.com/"),
    ("たけお歯科クリニック", "http://www.takeo-dc.com/"),
    ("谷川デンタルクリニック", "http://www.tanigawa-dentalclinic.com/"),
    ("徳丸歯科医院", "https://www.tokumaru-shika.com/"),
    ("医療法人きし歯科ファミリークリニック", "https://kishi-dental.com/"),
    ("大分矯正歯科", "https://oita-ortho.com/"),
    ("新港イトセ歯科", "https://www.itoseshika.com/"),
    ("しろくま歯科◇矯正歯科", "https://shirokuma-dental.jp/"),
    ("宮崎台デンタルクリニック", "https://miyazakidai-dc.com/"),
    ("宮崎マウスピース矯正歯科", "https://miyazaki-mouthpiece.com/"),
    ("松井たかし矯正歯科クリニック 宮崎橘通り分院", "https://happysmile-m.com/"),
    ("おか歯科", "http://www.okashika.jp/"),
    ("ななつ星歯科", "https://nanatsuboshi-shika.jp/"),
    ("しゃもとデンタルクリニック", "https://shamoto-dc.jp/"),
    ("SAKUデンタルクリニック", "https://saku-dc.com/"),
    ("医療法人篤志会 さこだ歯科", "https://tokushikai.jp/sakoda-dc/"),
    ("鹿児島セントラル歯科・矯正歯科", "http://centralkcc.jp/"),
    ("永田デンタルクリニック", "http://nagata-shika.net/"),
    ("田中矯正歯科", "http://hayanokai.com/"),
    ("えなつ歯科・矯正クリニック", "https://enatsu-dc.com/"),
    ("鹿児島ローズ歯科・矯正歯科 リュクス", "https://rose-smile.com/clinic-luxe"),
    ("鹿児島ローズ歯科・矯正歯科 アミュプラザ", "https://rose-smile.com/clinic-amu"),
    ("鹿児島こうづま歯科・矯正歯科", "http://ko-zuma.jp/m/"),
    ("松尾歯科･おとなこども矯正歯科", "http://www.matsuo-dc.info/"),
    ("のへじ矯正小児歯科", "https://noheji.kamiden.net/"),
    ("かみきたデンタルクリニック", "http://kamikita-ortho.com/"),
    ("たなべ歯科・矯正歯科医院", "https://www.tanabedc.jp/"),
    ("小林歯科医院", "https://www.kobayashi-dentistry.com/"),
    ("八戸総合歯科・矯正歯科", "https://www.n-yoshida.jp/"),
    ("盛岡となん歯科･こども矯正歯科", "https://tonandc.com/"),
    ("ゆいとぴあ歯科医院", "http://www.yuitopia-dc.com/"),
    ("村井産婦人科小児歯科医院", "https://murai-clinic.net/"),
    ("なごみ矯正・デンタルクリニック", "https://www.nagomi-dentalclinic.jp/"),
    ("ざいもくちょう歯科", "https://zmt-dc.com/"),
    ("泉中央おとなこども歯科・矯正歯科", "https://izumiokdc.hp.peraichi.com/"),
    ("仙台おとなこども歯科 矯正歯科", "https://sendaiotonakodomo-dental.com/"),
    ("上杉おとなこども歯科・矯正歯科", "https://kamisugi-otonakodomo.com/"),
    ("利府なのはなデンタルクリニック", "https://nanohana-dc-lp.com/"),
    ("坂井おとなこども歯科", "http://sakaiclinic.or.jp/"),
    ("たがじょうグリーン歯科", "http://www.tagajogreen.jp/"),
    ("仙台つつじがおか歯科", "https://sendai-tsutsuji.com/"),
    ("クニデンタルクリニック", ""),  # No website listed
    ("仙台リボン歯科・矯正歯科 インプラント", "https://ribon-shika.jp/sendai/"),
    ("くぼた矯正歯科クリニック", "https://kubota5888.com/"),
    ("仙台青葉矯正歯科クリニック", "https://dd-dentalclinic.jp/lp/ddd/lp01/"),
    ("仙台東口矯正歯科", "http://www.sendai-ortho.com/"),
    ("仙台キュア矯正歯科", "https://sendai-cure.jp/"),
    ("懸田歯科医院", "https://www.kaketa.com/"),
    ("クローバーデンタル", "https://www.cloverdental.com/"),
    ("むさしデンタルオフィス", "http://www.musashi-dent.jp/"),
    ("パール歯科クリニック", "https://pearl-shika-akita.com/"),
    ("医療法人BLESS さくら歯科医院 仙北市", "https://sakura-oral-health.com/"),
    ("ティーズデンタルオフィス 山形嶋南院", "http://tsdental.jp/"),
    ("まむろ歯科", "https://www.mamuro-dental.com/"),
    ("あきらデンタル・クリニック", "https://yamagata-shika.com/"),
    ("タクヤデンタルクリニック 山形嶋北院", "https://www.takuya-dental.com/"),
    ("永田歯科医院", "https://ndc2230.jp/"),
    ("ごとう歯科･矯正歯科クリニック", "https://www.goto-smile.com/"),
    ("医療法人社団 尚和会 とがし歯科医院", "https://www.togashi-dent.jp/"),
    ("南館歯科クリニック・矯正歯科", "https://www.minamidate-dental.com/"),
    ("米沢ファミリー歯科・矯正歯科", "http://www.yonezawafamily.jp/"),
    ("石田おさむ歯科医院", "https://www.ishidaosamu.com/"),
    ("須賀川みらい歯科クリニック", "https://www.mdc-s.com/"),
    ("アールエス矯正歯科", "https://www.rs-orthodontics.com/"),
    ("しんデンタルクリニック", "https://www.shin-dental.jp/"),
    ("カーナデンタル＆ビューティークリニック", "https://carnabeauty.com/"),
]


def extract_director_keywords(text: str) -> List[str]:
    """
    Extract potential director names from text using Japanese keywords.
    """
    keywords = ["院長", "理事長", "Dr.", "医学博士", "代表"]
    results = []

    for keyword in keywords:
        if keyword in text:
            # Extract context around keyword
            idx = text.find(keyword)
            start = max(0, idx - 50)
            end = min(len(text), idx + 100)
            context = text[start:end]
            results.append(context)

    return results


def clean_director_name(text: str) -> str:
    """Remove honorifics and clean the director name."""
    # Remove common honorifics
    remove_patterns = ["Dr.", "先生", "医学博士", "院長", "理事長"]

    for pattern in remove_patterns:
        text = text.replace(pattern, "")

    # Remove leading/trailing whitespace and punctuation
    text = text.strip().strip("：").strip("、").strip("。").strip()

    # Keep only the first occurrence if multiple names present
    if "、" in text:
        text = text.split("、")[0]
    if "、" in text:
        text = text.split("、")[0]

    return text


def process_clinic(clinic_name: str, website_url: Optional[str]) -> str:
    """
    Process a single clinic to extract director name.
    Returns director name or "不明" if not found.
    """

    # Placeholder for actual WebFetch/WebSearch implementation
    # This would normally call WebFetch first, then WebSearch as fallback

    # For now, return placeholder indicating data collection
    if not website_url or website_url == "":
        return "不明"

    # Return placeholder that indicates these need actual API calls
    return f"[PENDING: {clinic_name}]"


def main():
    """Main execution function."""

    # Output file path
    output_path = Path("/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04/director_names_batch_2.csv")

    # Prepare results
    results = []

    print(f"Processing {len(DENTAL_CLINICS)} dental clinics (rows 108-214)...")
    print(f"Output will be saved to: {output_path}")
    print()

    # Process each clinic
    for idx, (clinic_name, website_url) in enumerate(DENTAL_CLINICS, 1):
        row_num = 107 + idx  # Starting from row 108

        print(f"[{row_num}] Processing: {clinic_name}")

        # Process clinic
        director_name = process_clinic(clinic_name, website_url)

        # Add to results
        results.append({
            "row_number": row_num,
            "clinic_name": clinic_name,
            "website_url": website_url,
            "director_name": director_name
        })

        # Rate limiting: 2 seconds between requests
        if idx < len(DENTAL_CLINICS):
            time.sleep(2)

    # Write CSV
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['row_number', 'clinic_name', 'website_url', 'director_name'])
        writer.writeheader()
        writer.writerows(results)

    print()
    print(f"Results saved to: {output_path}")
    print(f"Total clinics processed: {len(results)}")

    return results


if __name__ == "__main__":
    results = main()
