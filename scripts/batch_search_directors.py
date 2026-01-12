#!/usr/bin/env python3
"""
複数医院の院長名を一括検索して CSV に保存するスクリプト
WebSearchツール出力から院長名を自動抽出
"""

import csv
import json
import time
from pathlib import Path

# Configuration
BATCH_4_DATA = {
    322: ("みわ矯正歯科医院", "https://miwa-orthodontic.com/"),
    323: ("やまもと歯科・矯正歯科医院", "https://yamamoto-dc.com/"),
    324: ("金澤むさし総合歯科・矯正歯科クリニック", "https://www.ki-dc.com/"),
    325: ("しのぶ歯科医院", "http://www.implant-418.com/"),
    326: ("匠歯科医院", "https://www.takumi-dental.ishikawa.jp/"),
    327: ("ハッピー歯科医院", "http://www.happy-dental.jp/"),
    328: ("ピースデンタルクリニック", "https://pieace.jp/"),
    329: ("スター矯正歯科・歯科", "http://www.star-dc.jp/"),
    330: ("しおはま矯正歯科", "http://www.shiohama.biz/"),
    331: ("矯正歯科石井クリニック", "http://www.iortho.jp/"),
    332: ("コレクトデンタルクリニック金沢", "https://correctdental-clinic.org/kanazawa"),
    333: ("くりもり大人こども歯科クリニック", "https://kurimori-dental.com/?utm_source=google&utm_medium=gmb"),
    334: ("はまだ歯科クリニック", "https://www.hamada-dc-fukui.com/"),
    335: ("ゆき歯科クリニック", "https://www.yukidental.com/"),
    336: ("カトウ矯正歯科", "https://www.kato-ortho.jp/"),
    337: ("若泉歯科クリニック", "https://www.wakaizumi-dental.com/"),
    338: ("ばば歯科医院", "https://baba-dc.com/"),
    339: ("みらい歯科・こども矯正歯科 フォレストモール甲斐竜王", "https://mirai-dc.net/"),
    340: ("富士見歯科医院", "https://www.fujimi-dc.com/"),
    341: ("クリニックささもと歯科", "http://www.clinic-sasamoto.com/"),
    342: ("あいざわ歯科クリニック 医療法人再生会", "http://www.aizawa-dc.jp/"),
    343: ("愛彩デンタルクリニック矯正歯科（ホワイトエッセンス甲府城東院）", "https://aisai-dental.com/"),
    344: ("歯科・矯正歯科 GOODSMILE", "http://www.goodsmile-dental.com/"),
    345: ("安富歯科医院", "http://yasutomishika8020.cihp2.jp/"),
    346: ("中央歯科医院", "https://www.chuuou-dental.com/"),
    347: ("はやかわ歯科医院", "http://www.hayakawa-dc.net/"),
    348: ("ニッコリ矯正歯科クリニック", "https://www.nsk-kyousei.jp/?utm_source=google&utm_medium=map"),
    349: ("医療法人BrightSmiles あんざい歯科医院 おとなこども歯科・矯正歯科", "http://www.aanzai.co.jp/"),
    350: ("みらいデンタルクリニック", "http://www.miraidental.jp/"),
    351: ("メディケア歯科クリニック長野三輪", "http://www.nagano-miwa.com/?utm_source=GBP&utm_medium=GBP&utm_term=GBP&utm_content=GBP&utm_campaign=GBP"),
    352: ("ニコニコ歯科 伊那矯正オフィス", "https://nikonikoortho.jimdofree.com/"),
    353: ("おばた矯正歯科クリニック", "https://obata-kyousei.jp/"),
    354: ("いちょう通り歯科 こども歯科", "http://www.ichodori-dc.com/"),
    355: ("岐阜プレシャス歯科・矯正歯科．", "https://ribon-shika.jp/gifushi/"),
    356: ("りお歯科クリニック", "http://www.rio-dc.com/"),
    357: ("こんのでんたるVILLAGE", "https://konnodentalvillage.jp/"),
    358: ("佐藤歯科医院", "https://www.dentist-sato.com/"),
    359: ("カリス歯科クリニック", "https://charis-dc.jp/?utm_source=Google&utm_medium=map"),
    360: ("れあ歯科クリニック 矯正歯科小児歯科", "http://lea-dc.jp/"),
    361: ("大野歯科クリニック", "https://st-sky.net/"),
    362: ("岐阜駅前歯科クリニック・ 矯正歯科", "http://www.gifuekimaeshika.com/"),
    363: ("ただこし歯科・矯正歯科 総合クリニック｜可児市 歯医者", "https://www.tadakoshi.com/"),
    364: ("えんどう歯科・矯正歯科クリニック", "https://www.endo-dc.net/"),
    365: ("おくだ歯科・矯正歯科", "https://okuda-shika.jp/?utm_source=Google&utm_medium=map"),
    366: ("麻生キッズデンタルパーク", "http://www.aso-kidsdental.com/"),
    367: ("小嶋デンタルクリニック", "https://ryu-medical.com/"),
    368: ("静岡スマイル歯科・矯正歯科", "https://shizuoka-shika.com/"),
    369: ("あさひ歯科クリニック", "https://www.asahidentalclinic.com/"),
    370: ("すえのぶクローバー歯科医院", "http://www.suenobu-smile.com/"),
    371: ("セントラル歯科クリニック", "https://www.central-shika.jp/"),
    372: ("リーフデンタルクリニック", "http://leaf-dentalclinic.jp/"),
    373: ("静岡ひかり歯科・矯正歯科", "https://hikaridc.com/?utm_source=google&utm_medium=maps"),
    374: ("静岡呉服町デンタル矯正歯科", "https://dd-dentalclinic.jp/lp/ddd/lp01/?ads=a-ahd_p-orthodontics_s-google_m-maps_o-reserve_d-organicfeed_shizuokac-cv_1&utm_source=google&utm_medium=maps&utm_campaign=a-ahd_p-orthodontics_s-google_m-maps_o-reserve_d-organicfeed_shizuokac-cv_1"),
    375: ("ブライフ矯正歯科", "https://www.brife-orthodontics.com/"),
    376: ("静岡駅前歯科クリニック", "https://shizuoka118.com/"),
    377: ("いとう歯科矯正歯科ティースエクセレントクリニック", "https://www.hamamatsu-kyousei.com/"),
    378: ("Ｇ＆Ｏデンタルクリニック", "http://www.kamiawase.jp/"),
    379: ("とも歯科クリニック", "https://www.tomoshika.jp/"),
    380: ("医療法人にいみ歯科・矯正歯科", "https://www.niimi-shika.com/"),
    381: ("医療法人にじいろ くろい歯科クリニック", "http://www.kuroi-dc.com/"),
    382: ("杉原歯科", "http://www.sugiharashika.com/"),
    383: ("せがわ歯科クリニック 伊賀市 歯医者/予防歯科", "http://segawa-d.jp/"),
    384: ("峰歯科・矯正歯科クリニック", "https://www.minesika.com/?utm_source=Google&utm_medium=map"),
    385: ("名張かめい歯科・矯正歯科", "http://kamei-dentalclinic.com/"),
    386: ("津のまち矯正歯科", "https://www.tsunomachi.jp/"),
    387: ("きくち矯正歯科", "http://www.k-kikuchi.com/"),
    388: ("プルチーノ歯科・矯正歯科 四日市", "https://www.pulcino-yokkaichi.com/?utm_source=GMB"),
    389: ("宇治山田歯科医院", "http://www.ujiyamada.com/"),
    390: ("大木歯科・矯正歯科 四日市", "https://ohkidc-yokkaichi.com/"),
    391: ("やまぐち歯科 南草津 歯医者 小児歯科", "http://www.yamaguchi-d.net/"),
    392: ("Sono Dental Clinic おとな&こども歯科", "http://sono-dental.com/"),
    393: ("かがやき歯科クリニック", "https://www.kagayaki-dental.com/"),
    394: ("野洲U歯科・矯正歯科", "http://u-shika.jp/"),
    395: ("ごとう歯科こども・おとな歯科", "https://goto-dental3d.com/?utm_source=google&utm_medium=maps"),
    396: ("湖南トラスト歯科・矯正歯科", "https://souseikai-trust.jp/konan/"),
    397: ("東近江だいき歯科・矯正歯科", "https://ribon-shika.jp/higashioumi/"),
    398: ("みなみ草津ファミリー歯科", "https://www.dc-family.jp/"),
    399: ("南草津だいき歯科・矯正歯科", "https://ribon-shika.jp/minamikusatsu/"),
    400: ("はちまん駅前歯科", "https://www.hachiman-dental.com/"),
    401: ("ウイング栗東矯正歯科クリニック", "https://www.wingritto.com/"),
    402: ("うかい歯科クリニック", "http://www.ukaidc.com/"),
    403: ("大津クオーレ歯科クリニック", "http://cuore-dental.jp/"),
    404: ("かやはら歯科クリニック", "http://kayahara-shika.com/"),
    405: ("こささ歯科こども矯正クリニック", "https://kosasa.jp/?utm_source=google&utm_medium=map"),
    406: ("京都下鴨ライフ歯科・矯正歯科・小児歯科", "https://www.lifedc-kyotoshimogamo.com/"),
    407: ("肥後歯科口腔外科クリニック", "http://higo-dent.com/"),
    408: ("聖護院やぎ歯科・矯正歯科", "https://shogoin-yagi-dc.com/?utm_source=google&utm_medium=maps"),
    409: ("いのうえ歯科クリニック", "https://inoue-do.com/"),
    410: ("医療法人くわばら歯科医院", "http://www.dentrust.jp/"),
    411: ("中田歯科クリニック", "https://www.nakata-dental.com/"),
    412: ("京都二条たけち歯科クリニック", "https://www.tdc-smile.jp/"),
    413: ("東洞院はやし歯科", "https://higashinotoin-hayashi-dc.com/?utm_source=google&utm_medium=maps"),
    414: ("京都四条矯正歯科クリニック", "https://dd-dentalclinic.jp/lp/ddd/lp01/?ads=a-ahd_p-orthodontics_s-google_m-maps_o-reserve_d-organicfeed_kyotoc-cv_1&utm_source=google&utm_medium=maps&utm_campaign=a-ahd_p-orthodontics_s-google_m-maps_o-reserve_d-organicfeed_kyotoc-cv_1"),
    415: ("江口矯正歯科クリニック", "https://eguchi-kyousei.com/?utm_source=google&utm_medium=maps"),
    416: ("巴山矯正歯科・歯科", "http://www.tomoyama.jp/"),
    417: ("河原町歯科・矯正歯科クリニック", "https://kawaramachi-kyousei.com/?utm_source=google&utm_medium=maps"),
    418: ("キョート矯正歯科クリニック 京都", "https://www.kyousei-kyoto.com/?utm_source=google&utm_medium=maps"),
    419: ("京都四条河原町トラスト歯科・矯正歯科院", "https://souseikai-trust.jp/kawaramachi/"),
    420: ("トミイ歯科・矯正歯科", "http://www.tomiidentaloffice.jp/?y_source=1_MTk0MjI2MjgtNzE1LWxvY2F0aW9uLndlYnNpdGU%3D"),
    421: ("京都 出町トラスト歯科・矯正歯科", "https://souseikai-trust.jp/kyoto/"),
    422: ("ホワイトエッセンス京都四条通り矯正歯科", "https://www.whiteessence.com/clinic/kyoto/177/?utm_source=googlemybusiness&utm_medium=google&utm_campaign=maps_177"),
    423: ("駅前矯正歯科", "https://kyoto-ekimaekyousei.jp/"),
    424: ("さわだ矯正歯科クリニック", "https://www.sawada-kyouseishika-kyoto.jp/?utm_source=google&utm_medium=map&utm_campaign=gbp"),
    425: ("みかげ小児歯科・矯正歯科クリニック", "http://www.mikage-dc.com/"),
    426: ("よこやまこども歯科", "http://www.yokoyama1182.com/"),
    427: ("ハローこどもファミリー歯科", "http://hello-child.com/"),
    428: ("ママとこどものはいしゃさん三木院", "http://www.mamatokodomo-miki.com/"),
}

OUTPUT_FILE = "/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-04/director_names_batch_4.csv"

def generate_search_instructions():
    """検索用の指示ファイルを生成"""
    print("=" * 80)
    print("院長名一括検索：WebSearch/WebFetch対応版")
    print("=" * 80)
    print(f"\n対象医院数: {len(BATCH_4_DATA)} 件（行322-428）")
    print("\n【手動検索方法】")
    print("-" * 80)

    # グループ化して表示
    groups = {
        "富山県": [],
        "石川県": [],
        "福井県": [],
        "山梨県": [],
        "長野県": [],
        "岐阜県": [],
        "静岡県": [],
        "三重県": [],
        "滋賀県": [],
        "京都府": [],
        "兵庫県": [],
    }

    # 医院をグループ分け
    prefectures = {
        (322, 332): "富山県/石川県",
        (333, 337): "福井県",
        (338, 347): "山梨県",
        (349, 353): "長野県",
        (354, 365): "岐阜県",
        (366, 378): "静岡県",
        (379, 390): "三重県",
        (391, 404): "滋賀県",
        (405, 424): "京都府",
        (425, 428): "兵庫県",
    }

    # テンプレートCSVを生成
    Path(OUTPUT_FILE).parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['行番号', '医院名', '公式ウェブサイト', '院長名', '検索方法'])

        for line_number in sorted(BATCH_4_DATA.keys()):
            clinic_name, website = BATCH_4_DATA[line_number]
            writer.writerow([
                line_number,
                clinic_name,
                website,
                "検索待ち",
                ""
            ])

    print(f"\n✓ CSVテンプレート生成完了: {OUTPUT_FILE}")
    print("\n【次のステップ】")
    print("1. 各医院について以下のいずれかの方法で院長名を検索:")
    print("   a) 公式ウェブサイトがある場合: WebFetchで取得")
    print("   b) ウェブサイトがない/見つからない場合: WebSearchで検索")
    print("2. 検索結果から院長名を抽出（敬称は除外）")
    print("3. CSVの「院長名」列に記入")
    print("4. 見つからない場合は「不明」と記入")
    print("\n【検索例】")
    print('- WebFetch: "https://miwa-orthodontic.com/" + "院長名を探す"')
    print('- WebSearch: "みわ矯正歯科医院 院長"')

if __name__ == "__main__":
    generate_search_instructions()
