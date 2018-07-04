-- phpMyAdmin SQL Dump
-- version 3.3.7
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2018 年 07 月 04 日 02:05
-- 服务器版本: 5.0.90
-- PHP 版本: 5.2.14

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `bili`
--

-- --------------------------------------------------------

--
-- 表的结构 `videomes`
-- 数据部分只截取了前几条
-- 自增主键dbno，设置是和disappear一样的，但是这两个表中的
-- dbno连接在一起是没有任何意义的
-- 相比disappear这个表多了一个view，就是视频播放量
-- videomes和disappear一样是数据插入本数据库的时间
-- 如果要用下面的sql语句建表记得把自增主键的23万改成0

CREATE TABLE IF NOT EXISTS `videomes` (
  `dbno` int(11) NOT NULL auto_increment,
  `aid` int(11) NOT NULL,
  `view` int(11) default NULL,
  `danmaku` int(11) default NULL,
  `reply` int(11) default NULL,
  `favorite` int(11) default NULL,
  `coin` int(11) default NULL,
  `share` int(11) default NULL,
  `now_rank` int(11) default NULL,
  `his_rank` int(11) default NULL,
  `no_reprint` int(11) default NULL,
  `copyright` int(11) default NULL,
  `insert_time` datetime NOT NULL,
  PRIMARY KEY  (`dbno`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=320893 ;

--
-- 转存表中的数据 `videomes`
--

INSERT INTO `videomes` (`dbno`, `aid`, `view`, `danmaku`, `reply`, `favorite`, `coin`, `share`, `now_rank`, `his_rank`, `no_reprint`, `copyright`, `insert_time`) VALUES
(261846, 3934631, 22289706, 2585767, 162947, 93192, 153646, 37513, 0, 4, 0, 2, '2018-05-17 15:17:23'),
(320298, 4033926, 18671452, 335026, 70211, 385684, 348448, 121421, 95, 1, 0, 1, '2018-05-19 15:43:01'),
(152605, 3749039, 16476904, 1567360, 94696, 73436, 58246, 18921, 0, 18, 0, 2, '2018-05-13 21:21:22'),
(267513, 3944301, 11058894, 697149, 16328, 90168, 35215, 31744, 0, 43, 0, 2, '2018-05-17 19:38:07'),
(19057, 3521416, 10867166, 2353093, 103048, 359621, 772666, 201032, 1, 1, 0, 1, '2018-05-08 12:20:23'),
(298625, 3997347, 9970269, 994368, 42529, 34248, 39162, 7066, 0, 27, 0, 2, '2018-05-18 20:59:54'),
(194475, 3818869, 7988913, 94631, 21813, 267381, 124965, 86605, 0, 2, 0, 1, '2018-05-15 09:26:17'),
(26970, 3534854, 7584926, 177764, 38258, 349231, 5904, 85263, 0, 5, 0, 2, '2018-05-08 18:10:32'),
(165935, 3770834, 7439198, 197746, 79248, 175559, 178943, 116788, 0, 5, 0, 1, '2018-05-14 08:29:49'),
(22516, 3527221, 7414409, 474046, 11839, 23817, 12812, 20199, 0, 311, 0, 2, '2018-05-08 14:50:35'),
(121718, 3696842, 7192324, 52691, 10035, 191026, 114840, 67428, 0, 1, 0, 1, '2018-05-12 18:31:27'),
(245077, 3905462, 5915788, 164272, 51548, 359728, 203452, 61869, 0, 2, 0, 1, '2018-05-17 01:13:29'),
(166257, 3771373, 5753387, 261240, 13280, 243942, 98305, 64155, 0, 13, 0, 1, '2018-05-14 08:43:41');