#!/usr/bin/env python3
"""Merge missing Chinese translations into intl_zh_Hans.arb, copying metadata from en.arb."""
import json, io

en = json.load(open('lib/l10n/intl_en.arb', encoding='utf-8'))
zh = json.load(open('lib/l10n/intl_zh_Hans.arb', encoding='utf-8'))

# key -> Simplified Chinese translation (98 keys)
T = {
  "open_up_next_hint": "打开「接下来播放」队列",
  "settings_auto_update_episodes_24hour": "每 24 小时",
  "settings_auto_update_episodes_48hour": "每 2 天",
  "playing_next_queue_label": "接下来播放",
  "discovery_categories_itunes": "全部,艺术,商业,喜剧,教育,小说,政府,健康与健身,历史,儿童与家庭,休闲,音乐,新闻,宗教与信仰,科学,社会与文化,体育,电视与电影,科技,真实犯罪",
  "discovery_categories_pindex": "全部,幕后花絮,另类,动物,动画,艺术,天文学,汽车,航空,棒球,篮球,美容,书籍,佛教,商业,职业,化学,基督教,气候,喜剧,评论,课程,手工艺,板球,加密货币,文化,每日,设计,纪录片,戏剧,地球,教育,娱乐,创业,家庭,奇幻,时尚,小说,电影,健身,食品,足球,游戏,园艺,高尔夫,政府,健康,印度教,历史,爱好,冰球,家居,教程,即兴,访谈,投资,伊斯兰教,日志,犹太教,儿童,语言,学习,休闲,生活,管理,漫画,营销,数学,医学,心理健康,音乐,自然,自然,新闻,非营利,营养,育儿,表演,个人,宠物,哲学,物理学,地方,政治,关系,宗教,评论,角色扮演,橄榄球,跑步,科学,自我提升,性,足球,社会,社会,心灵,体育,单口相声,故事,游泳,电视,桌面游戏,科技,网球,旅行,真实犯罪,视频游戏,视觉,排球,天气,荒野,摔跤",
  "auto_scroll_transcript_label": "跟随文稿",
  "transcript_why_not_url": "https://anytimeplayer.app/docs/anytime_transcript_support_en.html",
  "semantics_mini_player_header": "迷你播放器。向右滑动到播放/暂停按钮。激活以打开主播放器窗口",
  "semantics_episode_tile_collapsed": "单集列表项。显示图片、摘要和主要控件。",
  "semantics_episode_tile_expanded": "单集列表项。显示描述、主要控件和附加控件。",
  "semantics_episode_tile_collapsed_hint": "展开以查看更多详情和附加选项",
  "semantics_episode_tile_expanded_hint": "收起以显示摘要、下载和播放控件",
  "sleep_episode_label": "本集播完时",
  "sleep_minute_label": "{minutes} 分钟",
  "sleep_timer_label": "睡眠定时器",
  "podcast_options_overflow_menu_semantic_label": "选项菜单",
  "semantic_announce_searching": "正在搜索，请稍候。",
  "semantic_playing_options_expand_label": "打开播放选项滑块",
  "semantic_playing_options_collapse_label": "关闭播放选项滑块",
  "semantic_podcast_artwork_label": "播客封面图",
  "semantic_chapter_link_label": "章节网页链接",
  "semantic_current_chapter_label": "当前章节",
  "episode_filter_started_label": "已开始",
  "episode_filter_played_label": "已播放",
  "episode_filter_unplayed_label": "未播放",
  "episode_filter_no_episodes_title_label": "未找到单集",
  "episode_filter_no_episodes_title_description": "该播客没有符合你搜索条件和筛选的单集",
  "episode_filter_clear_filters_button_label": "清除筛选",
  "episode_filter_semantic_label": "筛选单集",
  "episode_sort_semantic_label": "对单集排序",
  "episode_sort_latest_first_label": "最新的在前",
  "episode_sort_earliest_first_label": "最早的在前",
  "episode_sort_alphabetical_ascending_label": "按字母 A-Z",
  "episode_sort_alphabetical_descending_label": "按字母 Z-A",
  "open_show_website_label": "打开节目网站",
  "refresh_feed_label": "刷新单集",
  "scrim_layout_selector": "关闭布局选择器",
  "now_playing_episode_position": "单集进度",
  "now_playing_episode_time_remaining": "剩余时间",
  "resume_button_label": "继续播放单集",
  "play_download_button_label": "播放已下载单集",
  "cancel_download_button_label": "取消下载",
  "episode_details_button_label": "显示单集信息",
  "scrim_sleep_timer_selector": "关闭睡眠定时器选择器",
  "scrim_speed_selector": "关闭播放速度选择器",
  "scrim_episode_details_selector": "关闭单集详情",
  "scrim_episode_sort_selector": "关闭单集排序",
  "scrim_episode_filter_selector": "关闭单集筛选",
  "search_episodes_label": "搜索单集",
  "settings_continuous_play_option": "连续播放",
  "settings_continuous_play_subtitle": "队列为空时自动播放该播客的下一集",
  "share_podcast_option_label": "分享播客",
  "share_episode_option_label": "分享单集",
  "episode_semantic_time_minute_remaining": "{minutes} 分钟后结束",
  "episode_semantic_time_second_remaining": "{seconds} 秒后结束",
  "episode_time_weeks_ago": "{weeks,plural, =1{1周前}other{{weeks}周前}}",
  "episode_semantic_time_weeks_ago": "{weeks,plural, =1{一周前}other{{weeks}周前}}",
  "episode_time_days_ago": "{days,plural, =1{1天前}other{{days}天前}}",
  "episode_semantic_time_days_ago": "{days,plural, =1{一天前}other{{days}天前}}",
  "episode_time_hours_ago": "{hours,plural, =1{1小时前}other{{hours}小时前}}",
  "episode_semantic_time_hours_ago": "{hours,plural, =1{1小时前}other{{hours}小时前}}",
  "episode_time_minutes_ago": "{minutes,plural, =1{1分钟前}other{{minutes}分钟前}}",
  "episode_semantic_time_minutes_ago": "{minutes,plural, =1{1分钟前}other{{minutes}分钟前}}",
  "episode_time_now": "刚刚",
  "label_megabytes": "兆字节",
  "label_megabytes_abbr": "MB",
  "label_episode_actions": "单集操作",
  "settings_podcast_management_divider_label": "播客管理",
  "settings_notification_divider_label": "通知",
  "settings_background_refresh_option": "后台刷新",
  "settings_background_refresh_option_subtitle": "在屏幕关闭时刷新单集。这会增加电量消耗。",
  "settings_refresh_notification_option": "刷新通知",
  "settings_refresh_notification_option_subtitle": "刷新单集时显示通知图标",
  "update_library_option": "刷新播客库",
  "library_sort_alphabetical_label": "按字母排序",
  "library_sort_date_followed_label": "按关注日期",
  "library_sort_unplayed_count_label": "未播放单集",
  "library_sort_latest_episodes_label": "最新单集",
  "semantic_unplayed_episodes_count": "{episodes,plural, =1{1 集未播放}other{{episodes} 集未播放}}",
  "semantic_new_episodes_count": "{episodes,plural, =1{1 集新节目}other{{episodes} 集新节目}}",
  "layout_selector_highlight_new_episodes": "突出显示新单集",
  "layout_selector_sort_by": "排序方式",
  "layout_selector_sort_by_alphabetical": "按字母",
  "layout_selector_sort_by_followed": "按关注",
  "layout_selector_sort_by_unplayed": "按未播放",
  "layout_selector_list_view": "列表视图",
  "layout_selector_grid_view": "网格视图",
  "layout_selector_compact_grid_view": "紧凑网格视图",
  "alert_sync_title_label": "播客库更新",
  "alert_sync_title_body": "Anytime 正在更新你的播客库",
  "podcast_context_play_latest_episode_label": "播放最新单集",
  "podcast_context_queue_latest_episode_label": "将最新单集加入队列",
  "label_podcast_actions": "播客操作",
  "podcast_context_play_next_episode_label": "播放下一集未播放单集",
  "podcast_context_queue_next_episode_label": "将下一集未播放单集加入队列",
  "settings_background_refresh_mobile_data_option": "使用移动数据时刷新",
  "settings_background_refresh_mobile_data_option_subtitle": "允许在使用移动数据时刷新播客库",
}

missing = [k for k in en if not k.startswith('@') and k not in zh]
not_present = [k for k in T if k not in missing]
applied = 0
for k in missing:
    if k in T:
        zh[k] = T[k]
        # copy metadata block from en
        if '@' + k in en:
            zh['@' + k] = json.loads(json.dumps(en['@' + k]))
        applied += 1

# write back preserving key order (english order for new keys)
ordered = {}
for k in en:
    if k.startswith('@'):
        continue
    if k in zh:
        ordered[k] = zh[k]
        if '@' + k in zh:
            ordered['@' + k] = zh['@' + k]
# any zh-only keys not in en
for k in zh:
    if k.startswith('@'):
        continue
    if k not in ordered:
        ordered[k] = zh[k]
        if '@' + k in zh:
            ordered['@' + k] = zh['@' + k]

with io.open('lib/l10n/intl_zh_Hans.arb', 'w', encoding='utf-8') as f:
    f.write(json.dumps(ordered, ensure_ascii=False, indent=2))
    f.write('\n')

print(f"缺失 {len(missing)} 条，已补 {applied} 条")
print(f"T 里有但本不在 missing 的 key: {not_present}")
new_missing = [k for k in en if not k.startswith('@') and k not in ordered]
print(f"补完后仍缺失: {len(new_missing)}")