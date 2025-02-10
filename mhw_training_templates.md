# Monster Hunter World Training Data Templates

This document outlines the question and response templates for creating a fine-tuned LLM focused on Monster Hunter World game data.

## Monster Templates

### Basic Monster Information
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World expert who provides detailed information about monsters."
    },
    {
      "role": "user",
      "content": "What kind of monster is [monster_name]?"
    },
    {
      "role": "assistant",
      "content": "[monster_name] is a [species] class monster. It is classified as a [size] monster and is [if_elder_dragon: an Elder Dragon][if_not_elder_dragon: part of the [monster_type] category]."
    }
  ]
}
```

### Monster Weaknesses
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World expert who provides detailed information about monsters."
    },
    {
      "role": "user",
      "content": "What are [monster_name]'s weaknesses?"
    },
    {
      "role": "assistant",
      "content": "[monster_name] is most vulnerable to [element1] (★★★) and [element2] (★★) attacks. For status effects, it's particularly susceptible to [status1]. Its most vulnerable body parts are the [weak_point1] and [weak_point2]."
    }
  ]
}
```

### Monster Rewards
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World expert who provides detailed information about monsters."
    },
    {
      "role": "user",
      "content": "What materials can I get from [monster_name]?"
    },
    {
      "role": "assistant",
      "content": "From [monster_name], you can obtain:\n- [material1] (Common reward, [drop_rate1]%)\n- [material2] (Rare reward, [drop_rate2]%)\n- [material3] (Break reward from [body_part])\n[if_plate_or_gem: The [rare_material] has a very low drop rate of [rare_drop_rate]% and is best obtained through investigations.]"
    }
  ]
}
```

## Quest Templates

### Quest Information
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World quest advisor."
    },
    {
      "role": "user",
      "content": "Tell me about the quest '[quest_name]'"
    },
    {
      "role": "assistant",
      "content": "'[quest_name]' is a [rank]★ [quest_type] quest. Location: [location]. Target: [monster_name]. Reward: [zenny]z and [reward_items]. Time limit: [time_limit] minutes. [if_special_conditions: Special conditions: [conditions]]"
    }
  ]
}
```

### Quest Requirements
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World quest advisor."
    },
    {
      "role": "user",
      "content": "What do I need to do to unlock '[quest_name]'?"
    },
    {
      "role": "assistant",
      "content": "To unlock '[quest_name]', you need:\n- Hunter Rank [required_rank] or higher\n[if_prerequisite_quests: - Complete the following quests first:\n  * [prerequisite1]\n  * [prerequisite2]]\n[if_special_requirement: - Additional requirement: [special_requirement]]"
    }
  ]
}
```

## Item Templates

### Item Information
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World item expert."
    },
    {
      "role": "user",
      "content": "What is [item_name] used for?"
    },
    {
      "role": "assistant",
      "content": "[item_name] is a [rarity]-star [item_type]. [item_description] [if_craftable: It can be crafted using [materials].][if_gathering: It can be gathered from [locations].][if_monster_part: It is obtained from [monster_name] by [obtain_method].]"
    }
  ]
}
```

### Crafting Information
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World crafting expert."
    },
    {
      "role": "user",
      "content": "How do I craft [item_name]?"
    },
    {
      "role": "assistant",
      "content": "To craft [item_name], you need:\n[for_each_material: - [quantity]x [material_name] ([source])]\nThis recipe produces [yield] [item_name][if_alternatives: . Alternative recipe available: [alternative_recipe]]"
    }
  ]
}
```

## Armor Templates

### Armor Stats
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World equipment expert."
    },
    {
      "role": "user",
      "content": "What are the stats of [armor_name]?"
    },
    {
      "role": "assistant",
      "content": "[armor_name] ([armor_type]) has:\n- Defense: [defense]\n- Resistances:\n  * Fire: [fire_res]\n  * Water: [water_res]\n  * Thunder: [thunder_res]\n  * Ice: [ice_res]\n  * Dragon: [dragon_res]\nSkills:\n[for_each_skill: - [skill_name] Level [skill_level]]"
    }
  ]
}
```

### Armor Set Information
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World equipment expert."
    },
    {
      "role": "user",
      "content": "Tell me about the [set_name] armor set"
    },
    {
      "role": "assistant",
      "content": "The [set_name] set consists of:\n[for_each_piece: - [piece_name] ([piece_type])]\nSet Bonus: [set_bonus_name] ([set_bonus_description])\nRequired pieces for bonus: [pieces_required]"
    }
  ]
}
```

## Weapon Templates

### Weapon Stats
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World weapon expert."
    },
    {
      "role": "user",
      "content": "What are the stats of [weapon_name]?"
    },
    {
      "role": "assistant",
      "content": "[weapon_name] ([weapon_type]):\n- Attack: [attack]\n[if_element: - Element: [element_type] [element_damage]]\n[if_affinity: - Affinity: [affinity]%]\n[if_sharpness: - Sharpness: [sharpness_levels]]\n[if_bowgun: - Ammo Types: [ammo_types]]\n[if_bow: - Coatings: [coating_types]]\nSlots: [slot_configuration]"
    }
  ]
}
```

### Weapon Crafting
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World weapon expert."
    },
    {
      "role": "user",
      "content": "How do I craft [weapon_name]?"
    },
    {
      "role": "assistant",
      "content": "To craft [weapon_name], you need:\n[for_each_material: - [quantity]x [material_name] ([source])]\nCost: [zenny]z\n[if_prerequisite: Requires previous weapon: [prerequisite_weapon]]"
    }
  ]
}
```

## Location Templates

### Location Information
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World location expert."
    },
    {
      "role": "user",
      "content": "What can I find in [location_name]?"
    },
    {
      "role": "assistant",
      "content": "[location_name] features:\nMonsters:\n[for_each_monster: - [monster_name] ([habitat_type])]\nGathering Points:\n[for_each_gathering_type: - [gathering_type]: [items_available]]\nCamps: [camp_locations]"
    }
  ]
}
```

## Multi-turn Conversation Examples

### Monster Hunting Strategy
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World expert who provides detailed hunting advice."
    },
    {
      "role": "user",
      "content": "I need help hunting [monster_name]"
    },
    {
      "role": "assistant",
      "content": "I can help you prepare for hunting [monster_name]. Would you like to know about its weaknesses, recommended equipment, or general strategy?"
    },
    {
      "role": "user",
      "content": "Tell me about the recommended equipment"
    },
    {
      "role": "assistant",
      "content": "For hunting [monster_name], I recommend:\nWeapon: [recommended_weapon_type] with [element] element\nArmor: [recommended_armor_set] for [armor_benefits]\nItems to bring:\n[for_each_item: - [item_name]: [item_purpose]]"
    }
  ]
}
```

### Quest Preparation
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World quest advisor."
    },
    {
      "role": "user",
      "content": "How should I prepare for '[quest_name]'?"
    },
    {
      "role": "assistant",
      "content": "For '[quest_name]', here's what you need to know:\nTarget: [monster_name]\nLocation: [location_name]\nRecommended equipment:\n[equipment_recommendations]\nRequired items:\n[item_recommendations]\nSpecial considerations: [special_notes]"
    },
    {
      "role": "user",
      "content": "What items should I bring?"
    },
    {
      "role": "assistant",
      "content": "Essential items for this quest:\n[for_each_item: - [item_name]: [item_purpose]]\nOptional but helpful:\n[for_each_optional_item: - [item_name]: [item_benefit]]"
    }
  ]
}
