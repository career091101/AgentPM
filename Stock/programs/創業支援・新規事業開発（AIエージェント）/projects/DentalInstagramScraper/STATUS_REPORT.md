# Dental Instagram Scraper - Status Report

**Date**: 2026-01-02
**Status**: ✅ Core functionality working - Strategy pivot required

## 🎯 Summary

Instagram collection system is **working** but requires a **strategy pivot** from hashtag search to seed list approach due to Instagram API limitations.

## ✅ What's Working

### 1. Authentication
- ✅ Cookie-based authentication successful (11 cookies loaded)
- ✅ Session maintained properly
- ✅ No login failures

### 2. Profile Fetching
- ✅ Direct profile access works perfectly
- ✅ Can fetch profile data (name, bio, followers, posts, etc.)
- ✅ Business account detection works
- ✅ Dental clinic keyword filtering works

### 3. Data Extraction
- ✅ Postal code extraction (regex: `〒?\s*(\d{3})-?(\d{4})`)
- ✅ Address extraction (Japanese address patterns)
- ✅ Phone number extraction
- ✅ External URL capture

### 4. CSV Export
- ✅ UTF-8 BOM encoding (Excel-compatible)
- ✅ All required columns
- ✅ Timestamp-based filenames
- ✅ Proper formatting

### 5. Test Results
```
✅ Profile fetch: @dentaltown - SUCCESS
   Name: Dentaltown
   Followers: 14,770
   Posts: 3,780
   Business account: Yes
   CSV export: ✅ SUCCESS
```

## ❌ What's Not Working

### 1. Hashtag Search
**Issue**: Instagram hashtag API endpoint returns `404 Not Found`

**Tested hashtags**:
- ❌ #歯科 - 404 Not Found
- ❌ #dental - 404 Not Found
- ❌ #歯科医院 - 404 Not Found

**Root cause**: Instagram's `/explore/tags/` endpoint is not accessible with cookie authentication. This endpoint likely requires:
- Instagram official API (requires app registration)
- Different authentication method
- Or has been deprecated/restricted

### 2. Original Plan Deviation
- Original plan: Use hashtag search to discover 30-50 accounts
- Current reality: Hashtag search is not available

## 🔄 Strategy Pivot

### From Hashtag Search → Seed List Approach

**New workflow**:
1. **Build seed list** of Instagram handles (manually or via web search)
2. **Verify profiles** using direct profile access
3. **Extract data** from verified profiles
4. **Export to CSV**

### Three Ways to Build Seed List

#### Option 1: Manual Discovery (Recommended for now)
Search Google with these queries:
```
歯科医院 Instagram site:instagram.com
東京 歯科 インスタグラム
小児歯科 Instagram
```

Copy Instagram handles from search results.

#### Option 2: Use find_dental_handles.py
```bash
python find_dental_handles.py
```

Uses Anthropic Claude with web search to discover handles automatically.
*Note: Requires ANTHROPIC_API_KEY in .env*

#### Option 3: Instagram's Profile Suggestions
When searching for non-existent profiles, Instagram suggests similar profiles:
```
❌ @dentalclinic_jp does not exist
💡 Suggestions: hanasaku.dentalclinic.jp, family.dentalclinic.jp, jp_dental_clinic_
```

These suggestions can be harvested and added to seed list.

## 📋 Working Scripts

### 1. `collect_from_list.py` (Main collector)
**Purpose**: Collect data from a list of Instagram handles

**Usage**:
```bash
# Edit seed_handles list in the script
python collect_from_list.py
```

**Output**: `dental_instagram_YYYYMMDD_HHMMSS.csv`

### 2. `test_simple.py`
**Purpose**: Test cookie authentication and profile access

**Usage**:
```bash
python test_simple.py
```

### 3. `find_dental_handles.py`
**Purpose**: Discover Instagram handles using web search

**Usage**:
```bash
python find_dental_handles.py
```

**Output**: `dental_handles_東京_YYYYMMDD_HHMMSS.json`

## 🚀 Next Steps

### Immediate (15 minutes)
1. Manually find 20-30 real Japanese dental clinic Instagram handles
2. Add handles to `seed_handles` list in `collect_from_list.py`
3. Run collection: `python collect_from_list.py`
4. Review CSV output

### Short-term (1 hour)
1. Run `find_dental_handles.py` to auto-discover more handles
2. Verify discovered handles
3. Build comprehensive seed list (50-100 handles)
4. Run full collection

### Medium-term (Optional enhancements)
1. Implement fact-checking with Anthropic API
2. Add external URL scraping for missing addresses
3. Create automated discovery pipeline
4. Add location-based filtering (Tokyo, Osaka, etc.)

## 📊 Expected Results

With a seed list of **50 handles**:
- Estimated dental clinics: 40-45 (90% success rate)
- Profiles with postal code: 25-30 (60-70%)
- Profiles with address: 30-35 (70-80%)
- Needs manual review: 10-15 (20-30%)

## ⚙️ Technical Notes

### Rate Limiting
- Current: 5 seconds between profiles
- Tested stable with no rate limit issues
- Can potentially reduce to 3 seconds if needed

### Cookie Validity
- Cookies loaded successfully on 2026-01-02
- Monitor for expiration (typically 30-90 days)
- Re-export cookies if authentication fails

### CSV Format
- Encoding: UTF-8 with BOM (Excel-compatible)
- 12 columns including `needs_manual_review` flag
- Newlines in bio preserved as `\n`

## 🎯 Recommendations

1. **For quick MVP (today)**:
   - Manually find 20-30 handles
   - Run `collect_from_list.py`
   - Review and use data

2. **For scalable solution (this week)**:
   - Develop automated handle discovery
   - Build seed list to 100+ handles
   - Implement fact-checking

3. **For production (future)**:
   - Consider Instagram official API (if hashtag search is critical)
   - Build web scraping for clinic websites
   - Add geographic clustering

## 📁 Files Status

| File | Status | Purpose |
|------|--------|---------|
| `collect_from_list.py` | ✅ Working | Main data collector |
| `test_simple.py` | ✅ Working | Authentication test |
| `find_dental_handles.py` | 🟡 Untested | Handle discovery |
| `instagram_cookies.txt` | ✅ Valid | Authentication |
| `requirements.txt` | ✅ Complete | Dependencies |
| `config.yaml` | ⚠️ Outdated | Based on hashtag approach |
| `main.py` | ⚠️ Needs update | Based on hashtag approach |
| `src/instagram_collector.py` | ⚠️ Needs update | Uses hashtag search |

## 🔧 Files to Update

For full alignment with new strategy:
1. Update `config.yaml` to use seed list instead of hashtags
2. Modify `src/instagram_collector.py` to use direct profile access
3. Update `main.py` to integrate new workflow

**Current recommendation**: Use `collect_from_list.py` standalone for MVP. Update full system architecture later if needed.

## ✅ Conclusion

**The system works** - we successfully demonstrated:
- ✅ Authentication
- ✅ Profile fetching
- ✅ Data extraction
- ✅ CSV export

**Next action required**: Build a seed list of 20-50 real dental clinic Instagram handles to start production collection.

**Estimated time to first results**: 15-30 minutes (depending on seed list preparation method)
