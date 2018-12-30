/*
 Navicat Premium Data Transfer

 Source Server         : chwy.db
 Source Server Type    : SQLite
 Source Server Version : 2008017
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 2008017
 File Encoding         : 65001

 Date: 30/12/2018 14:57:38
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for Organization
-- ----------------------------
DROP TABLE "Organization";
CREATE TABLE "Organization" (
  "id" INTEGER NOT NULL,
  "name" TEXT,
  "parentId" INTEGER,
  "decsription" TEXT,
  CONSTRAINT "id" PRIMARY KEY ("id")
);

-- ----------------------------
-- Records of Organization
-- ----------------------------
BEGIN;
INSERT INTO "Organization" VALUES (1, '彩虹物业总公司', 0, '');
INSERT INTO "Organization" VALUES (2, '人事行政中心', 1, '');
INSERT INTO "Organization" VALUES (3, '彩虹城项目', 1, '');
INSERT INTO "Organization" VALUES (4, '客服部', 3, '');
INSERT INTO "Organization" VALUES (5, '维修部', 3, '');
COMMIT;

PRAGMA foreign_keys = true;
