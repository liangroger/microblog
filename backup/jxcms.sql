CREATE DATABASE IF NOT EXISTS jxcms DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
USE jxcms;


/* 用户表 */
DROP TABLE IF EXISTS sys_user;
CREATE TABLE sys_user (
  id int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
  lastlogintime datetime DEFAULT NULL COMMENT '登录时间',
  password varchar(32) NOT NULL COMMENT '密码',
  name varchar(30) DEFAULT NULL COMMENT '显示的名字',
  role smallint(6) NOT NULL DEFAULT 0 COMMENT '角色',
  loginname varchar(30) NOT NULL COMMENT '登录名',
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/* 
 jeesite中关于cms的库表
*/

DROP TABLE IF EXISTS cms_article;
DROP TABLE IF EXISTS cms_article_data;
DROP TABLE IF EXISTS cms_category;

DROP TABLE IF EXISTS cms_link;
DROP TABLE IF EXISTS cms_site;
/* Create Tables */

CREATE TABLE cms_article
(
    id int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
    category_id int(11) NOT NULL COMMENT '栏目编号',
    title varchar(255) NOT NULL COMMENT '标题',
    link varchar(255) COMMENT '文章链接',
    image varchar(255) COMMENT '文章图片',
    keywords varchar(255) COMMENT '关键字',
    description varchar(255) COMMENT '描述、摘要',
    weight int DEFAULT 0 COMMENT '权重，越大越靠前',
    weight_date datetime COMMENT '权重期限',
    hits int DEFAULT 0 COMMENT '点击数',
    create_by int(11) COMMENT '创建者',
    create_date datetime COMMENT '创建时间',
    update_by int(11) COMMENT '更新者',
    update_date datetime COMMENT '更新时间',
    del_flag char(1) DEFAULT '0' NOT NULL COMMENT '删除标记',
    PRIMARY KEY (id)
) COMMENT = '文章表';


CREATE TABLE cms_article_data
(
    id int(11) NOT NULL COMMENT '编号',
    content text COMMENT '文章内容',
    PRIMARY KEY (id)
) COMMENT = '文章详表';


CREATE TABLE cms_category
(
    id int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
    parent_id int(11) NOT NULL COMMENT '父级编号',
    parent_ids varchar(2000) NOT NULL COMMENT '所有父级编号',
    name varchar(100) NOT NULL COMMENT '栏目名称',
    image varchar(255) COMMENT '栏目图片',
    description varchar(255) COMMENT '描述',
    keywords varchar(255) COMMENT '关键字',
    sort int DEFAULT 30 COMMENT '排序（升序）',
    in_menu char(1) DEFAULT '1' COMMENT '是否在导航中显示（1：显示；0：不显示）',
	in_list char(1) DEFAULT '1' COMMENT '是否在分类页中显示列表（1：显示；0：不显示）',
	show_modes char(1) DEFAULT '0' COMMENT '展现方式（0:有子栏目显示栏目列表，无子栏目显示内容列表;1：首栏目内容列表；2：栏目第一条内容）',
    is_audit char(1) DEFAULT '1' COMMENT '是否需要审核',
    create_by int(11) COMMENT '创建者',
    create_date datetime COMMENT '创建时间',
    update_by int(11) COMMENT '更新者',
    update_date datetime COMMENT '更新时间',
    remarks varchar(255) COMMENT '备注信息',
    del_flag char(1) DEFAULT '0' NOT NULL COMMENT '删除标记',
    PRIMARY KEY (id)
) COMMENT = '栏目表';

CREATE TABLE cms_link
(
    id int(11) NOT NULL AUTO_INCREMENT COMMENT '编号',
    category_id int(11) NOT NULL COMMENT '栏目编号',
    title varchar(255) NOT NULL COMMENT '链接名称',
    image varchar(255) COMMENT '链接图片',
    href varchar(255) COMMENT '链接地址',
    weight int DEFAULT 0 COMMENT '权重，越大越靠前',
    weight_date datetime COMMENT '权重期限',
    create_by int(11) COMMENT '创建者',
    create_date datetime COMMENT '创建时间',
    update_by int(11) COMMENT '更新者',
    update_date datetime COMMENT '更新时间',
    remarks varchar(255) COMMENT '备注信息',
    del_flag char(1) DEFAULT '0' NOT NULL COMMENT '删除标记',
    PRIMARY KEY (id)
) COMMENT = '友情链接';

CREATE TABLE cms_site
(
	id int(11) NOT NULL AUTO_INCREMENT NOT NULL COMMENT '编号',
	name varchar(100) NOT NULL COMMENT '站点名称',
	title varchar(100) NOT NULL COMMENT '站点标题',
	logo varchar(255) COMMENT '站点Logo',
	domain varchar(255) COMMENT '站点域名',
	description varchar(255) COMMENT '描述',
	keywords varchar(255) COMMENT '关键字',
	theme varchar(255) DEFAULT 'default' COMMENT '主题',
	copyright text COMMENT '版权信息',
	custom_index_view varchar(255) COMMENT '自定义站点首页视图',
	create_by int(11) COMMENT '创建者',
	create_date datetime COMMENT '创建时间',
	update_by int(11) COMMENT '更新者',
	update_date datetime COMMENT '更新时间',
	remarks varchar(255) COMMENT '备注信息',
	del_flag char(1) DEFAULT '0' NOT NULL COMMENT '删除标记',
	PRIMARY KEY (id)
) COMMENT = '站点表';


/* Create Indexes */

CREATE INDEX cms_article_create_by ON cms_article (create_by ASC);
CREATE INDEX cms_article_title ON cms_article (title ASC);
CREATE INDEX cms_article_keywords ON cms_article (keywords ASC);
CREATE INDEX cms_article_del_flag ON cms_article (del_flag ASC);
CREATE INDEX cms_article_weight ON cms_article (weight ASC);
CREATE INDEX cms_article_update_date ON cms_article (update_date ASC);
CREATE INDEX cms_article_category_id ON cms_article (category_id ASC);
CREATE INDEX cms_category_parent_id ON cms_category (parent_id ASC);

CREATE INDEX cms_category_name ON cms_category (name ASC);
CREATE INDEX cms_category_sort ON cms_category (sort ASC);
CREATE INDEX cms_category_del_flag ON cms_category (del_flag ASC);

CREATE INDEX cms_link_category_id ON cms_link (category_id ASC);
CREATE INDEX cms_link_title ON cms_link (title ASC);
CREATE INDEX cms_link_del_flag ON cms_link (del_flag ASC);
CREATE INDEX cms_link_weight ON cms_link (weight ASC);
CREATE INDEX cms_link_create_by ON cms_link (create_by ASC);
CREATE INDEX cms_link_update_date ON cms_link (update_date ASC);
