/* 
 Records of sys_user
*/
INSERT INTO sys_user VALUES ('1',  '2014-11-20 21:15:56', 'e10adc3949ba59abbe56e057f20f883e', '业务员', '0', 'test');
INSERT INTO sys_user VALUES ('2',  '2014-08-04 15:35:01', 'e10adc3949ba59abbe56e057f20f883e', '管理员', '1', 'admin');

INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (1,0,'','首页','1','0');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (2,0,'','商务签证','1','0');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (3,0,'','签证办理','1','1');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (4,0,'','出境服务','1','1');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (5,0,'','了解带你飞','1','1');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (6,0,'','最新资讯','1','1');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (7,0,'','会员俱乐部','1','1');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (8,0,'','联系我们','1','1');

INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (9,3,'3','旅游签证','0','0');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (10,3,'3','探亲签证','0','0');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (11,3,'3','访问签证','0','0');

INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (12,4,'4','国际机票','0','0');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (13,4,'4','境外保险','0','0');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (14,4,'4','酒店接待','0','0');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (15,4,'4','其他服务','0','0');

INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (16,5,'5','公司介绍','0','0');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (17,5,'5','企业文化','0','0');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (18,5,'5','员工风采','0','0');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (19,5,'5','荣誉资质','0','0');

INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (20,6,'6','旅游资讯','0','0');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (21,6,'6','公司动态','0','0');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (22,6,'6','行业新闻','0','0');

INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (23,7,'7','客户见证','0','0');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (24,7,'7','往期风采','0','0');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (25,7,'7','会员福利','0','0');

INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (26,8,'8','常见问答','0','0');
INSERT INTO cms_category(id,parent_id,parent_ids,name,in_menu,in_list)  VALUES (27,8,'8','在线带你飞','0','0');

