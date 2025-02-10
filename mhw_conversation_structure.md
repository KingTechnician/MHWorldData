# Monster Hunter World Conversation Structure

This document outlines the conversation flow and structure for the Monster Hunter World build advisor system.

## Build Registration Process

### Initial Build Registration
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World build advisor who helps players optimize their equipment."
    },
    {
      "role": "user",
      "content": "I want to register my current equipment"
    },
    {
      "role": "assistant",
      "content": "I'll help you register your build. Please tell me your current equipment, starting with your weapon."
    },
    {
      "role": "user",
      "content": "I'm using the Defender Greatsword V"
    },
    {
      "role": "assistant",
      "content": "Got it. Now, please list your armor pieces (head, chest, arms, waist, legs)."
    },
    {
      "role": "user",
      "content": "I'm wearing full Guardian armor"
    },
    {
      "role": "assistant",
      "content": "I've registered your build:\nWeapon: Defender Greatsword V\nArmor Set: Guardian Set\nThis gives you:\n- Defense: [total_defense]\n- Skills: [skill_list]\nWould you like me to analyze this build or suggest improvements?"
    }
  ]
}
```

### Build Context Maintenance
The system maintains the following information about the user's build throughout the conversation:

1. Equipment Details
   - Weapon type and specific weapon
   - Armor pieces and set bonuses
   - Decorations and charms
   - Total defense and resistances
   - Active skills and their levels

2. Build Characteristics
   - Primary damage type (Raw/Elemental)
   - Key defensive capabilities
   - Mobility factors
   - Special mechanics (e.g., Guard capabilities, Evasion window)

## Analysis Patterns

### Basic Build Analysis
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World build advisor analyzing a player's registered equipment."
    },
    {
      "role": "user",
      "content": "What are my build's strengths?"
    },
    {
      "role": "assistant",
      "content": "Based on your current build:\n\nStrengths:\n1. [strength1] due to [skill/equipment]\n2. [strength2] from [skill/equipment]\n\nPotential Weaknesses:\n1. [weakness1] which could be improved by [suggestion1]\n2. [weakness2] which could be addressed with [suggestion2]"
    }
  ]
}
```

### Monster-Specific Analysis
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World build advisor analyzing a player's equipment for specific monsters."
    },
    {
      "role": "user",
      "content": "How well will my build work against Nergigante?"
    },
    {
      "role": "assistant",
      "content": "Analyzing your build versus Nergigante:\n\nAdvantages:\n- Your [defense_stat] is sufficient for surviving dive bombs\n- [skill1] will help with [specific_mechanic]\n\nChallenges:\n- Consider adding [suggested_skill] to better handle [monster_attack]\n- Your [current_resistance] might be low for [element_attack]"
    }
  ]
}
```

## Build Improvement Flow

### Targeted Improvements
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World build advisor suggesting specific improvements."
    },
    {
      "role": "user",
      "content": "How can I improve my defense against Teostra?"
    },
    {
      "role": "assistant",
      "content": "Looking at your current build versus Teostra:\n\nImmediate Improvements:\n1. Replace [current_piece] with [suggested_piece] for better fire resistance\n2. Add [decoration] to boost [relevant_skill]\n\nLong-term Goals:\n1. Farm [monster] for [material] to craft [upgrade]\n2. Work towards [set_bonus] for additional protection"
    }
  ]
}
```

### Progressive Build Path
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World build advisor creating upgrade paths."
    },
    {
      "role": "user",
      "content": "What should I work towards next with my build?"
    },
    {
      "role": "assistant",
      "content": "Based on your current build, here's your upgrade path:\n\nNext Steps:\n1. Farm [monster1] for [material1] to craft [upgrade1]\n2. Replace [current_piece] with [better_piece]\n\nFuture Goals:\n1. Work towards [endgame_piece] for [benefit]\n2. Add [decoration] when available"
    }
  ]
}
```

## Special Cases

### Incomplete Build Registration
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World build advisor handling incomplete build information."
    },
    {
      "role": "user",
      "content": "I have the Defender Greatsword but I'm not sure about my armor skills"
    },
    {
      "role": "assistant",
      "content": "I can help with partial build analysis. For your Defender Greatsword:\n\nRecommended Skills:\n1. [skill1] for [benefit1]\n2. [skill2] for [benefit2]\n\nWould you like suggestions for armor pieces that provide these skills?"
    }
  ]
}
```

### Mixed Set Optimization
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World build advisor specializing in mixed set optimization."
    },
    {
      "role": "user",
      "content": "How can I mix different armor pieces to maximize Attack Boost?"
    },
    {
      "role": "assistant",
      "content": "For maximizing Attack Boost with your current equipment access:\n\nRecommended Mix:\n- Head: [head_piece] ([skills])\n- Chest: [chest_piece] ([skills])\n- Arms: [arms_piece] ([skills])\n- Waist: [waist_piece] ([skills])\n- Legs: [legs_piece] ([skills])\n\nThis combination provides:\n- Attack Boost Level [level]\n- Additional Skills: [other_skills]\n- Set Bonuses: [if_any]"
    }
  ]
}
```

## Weapon-Specific Advice

### Weapon Playstyle Adaptation
```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a Monster Hunter World build advisor specializing in weapon-specific strategies."
    },
    {
      "role": "user",
      "content": "What skills should I focus on for Greatsword?"
    },
    {
      "role": "assistant",
      "content": "For Greatsword builds, prioritize:\n\nCore Skills:\n1. [skill1]: [benefit1]\n2. [skill2]: [benefit2]\n\nComfort Skills:\n1. [skill3]: [benefit3]\n2. [skill4]: [benefit4]\n\nBased on your current build, focus on obtaining:\n1. [missing_skill1] through [suggestion1]\n2. [missing_skill2] through [suggestion2]"
    }
  ]
}
```

## Context-Aware Responses

The system should maintain awareness of:

1. Player Progress
   - Current Hunter Rank
   - Story progression
   - Available quests/monsters

2. Equipment Access
   - Currently available gear
   - Craftable upgrades
   - Future equipment to work towards

3. Build History
   - Previous equipment setups
   - Past recommendations
   - Progression path

4. Playstyle Preferences
   - Preferred weapon types
   - Aggressive vs defensive playstyle
   - Solo vs multiplayer focus

This context helps provide more relevant and personalized advice throughout the conversation.
