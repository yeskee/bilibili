-- phpMyAdmin SQL Dump
-- version 3.3.7
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2018 年 07 月 04 日 01:55
-- 服务器版本: 5.0.90
-- PHP 版本: 5.2.14

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `bili`
-- 这个表是在播放页面爬取的视频信息的表
-- dbno是数据库内部设置的自增主键
-- uploaderno是上传视频的up主的号码
-- label是视频的标签，比如娱乐-Korea相关 什么的，存的都是网页原始的代码
-- videoneme就是视频名了，之前某个符号存储的时候会出错，然后被我替换成了一个
-- 相似的符号，' `好像就是这两个符号。都是英文打出来的。
-- uploadtime就是上传时间

-- --------------------------------------------------------

--
-- 表的结构 `videolabel`
--

CREATE TABLE IF NOT EXISTS `videolabel` (
  `dbno` int(11) NOT NULL,
  `uploaderno` int(11) NOT NULL,
  `label` varchar(25) character set ucs2 collate ucs2_unicode_ci NOT NULL,
  `videoname` varchar(160) character set utf8 collate utf8_unicode_ci NOT NULL,
  `uploadtime` datetime NOT NULL,
  PRIMARY KEY  (`dbno`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- 转存表中的数据 `videolabel`
--

INSERT INTO `videolabel` (`dbno`, `uploaderno`, `label`, `videoname`, `uploadtime`) VALUES
(1, 2027557, 'cinephile/montage', '【中文字幕】RocketJump: The Show 第1集【SCKC v0.5.1】', '2016-01-01 00:00:00'),
(2, 232720, 'douga/mmd', '【弹丸MMD】Music Music 【日向创诞生祭2016】', '2016-01-01 00:00:00'),
(3, 4851562, 'douga/mmd', '南北组融合【金丝雀旗袍 乐正绫&amp;洛天依】—Killer Lady .720p', '2016-01-01 00:00:00'),
(4, 97126, 'game/mugen', '【MUGEN】2016拜年庆', '2016-01-01 00:00:01'),
(5, 8400205, 'douga/other', '【海贼王】艾斯生日快乐！！！！永远的尼桑！！！', '2016-01-01 00:00:04'),
(6, 138252, 'cinephile/trailer_info', '【SLOMO】漫威第二阶段蓝光典藏花絮&amp;删减片段合集【双语字幕】', '2016-01-01 00:00:05'),
(7, 8904529, 'game/stand_alone', '新年快乐！大家都要开开心心的哦！！！  thanks for 2015！！！！！！！！！！！！', '2016-01-01 00:00:10'),
(8, 436329, 'anime/offical', '【完结】【Drama】虽然任性却很可爱\\任性可爱的小情人（福山润+下野紘）', '2016-01-01 00:00:17'),
(9, 237838, 'music/cover', '【芋头】小幸运【2周年贺曲】', '2016-01-01 00:00:17'),
(10, 4190684, 'dance/otaku', '【赤间菀枫】小小鹿  新年快乐', '2016-01-01 00:00:31'),
(11, 5101721, 'cinephile/montage', '【生田斗真】夜的第七章', '2016-01-01 00:00:47'),
(12, 1445803, 'music/cover', '【甜酱翻唱】LAMB☆诈尸的元旦贺~', '2016-01-01 00:00:48'),
(13, 6081193, 'game/mugen', '【私改】铃仙：教练我要打篮球！', '2016-01-01 00:00:49'),
(14, 3421632, 'game/stand_alone', '[跨年稿]传送门2（Portal 2）实况', '2016-01-01 00:00:50'),
(16, 9933164, 'ent/star', 'SNH48跨年公演《糖》', '2016-01-01 00:01:05'),
(17, 212891, 'douga/mad', '【治愈】相遇在那个桜色的季节', '2016-01-01 00:01:16'),
(18, 1813072, 'douga/mad', '【一拳超人/燃系】因为我是英雄啊！', '2016-01-01 00:01:19'),
(19, 3527182, 'ent/variety', '【Hey!Say!JUMP】151230 攻顶SUPER HIGH JUMP（高清中字）', '2016-01-01 00:01:38'),
(20, 585571, 'dance/otaku', '【阿卡】CLAP HIP CHERRY♥2016也一起前行吧♥', '2016-01-01 00:01:53'),
(21, 18414475, 'ent/korea', '[2Blegend] 新年快乐 ! From INFINITE 精效中字', '2016-01-01 00:02:04'),
(22, 4980074, 'game/online', '【音奏】跨年小插曲', '2016-01-01 00:02:12'),
(23, 3977500, 'life/daily', '【APH/COS】海英不明意义的视频测试x', '2016-01-01 00:02:14'),
(24, 5350996, 'game/stand_alone', '【钥匙解说】【我们身边的狼】第一章：和樵夫嘿嘿嘿 01', '2016-01-01 00:02:34'),
(25, 5919574, 'dance/otaku', '【蓝德×惜惜】Glide【真·广场舞】', '2016-01-01 00:03:23'),
(26, 14658998, 'game/online', '龙之谷华中一区烟雨工会纪念视频 强大剧情向+轻松日常！', '2016-01-01 00:03:25'),
(27, 17786184, 'kichiku/guide', '【枪声】大杂烩（元旦快乐）', '2016-01-01 00:03:48');