# Ara " def AddItemData(self, itemVnum, metinSlot "
# Tekrar ara

		self.__AdjustMaxWidth(attrSlot, itemDesc)

# Altına Ekle

		if chr.IsGameMaster(0):
			self.AppendTextLine("Vnum: (%d), Type: (%d), SubType: (%d)" % (itemVnum, itemType, itemSubType), self.TOOLTIP_STUFF_COLOR)
			self.AppendSpace(5)

# Ara " def __SetSkillTitle(self, skillIndex, skillGrade): "
# Hemen altına ekle

		if chr.IsGameMaster(0):
			self.AppendTextLine("Skill Vnum: (%d)" % skillIndex, self.TOOLTIP_STUFF_COLOR)
			self.AppendSpace(5)

# Ara

	NEED_SKILL_POINT_COLOR = 0xff9A9CDB

# Altına ekle

	TOOLTIP_STUFF_COLOR = 0xffABFFF6