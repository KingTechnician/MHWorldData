import json
import pandas as pd
from tqdm import tqdm
from pathlib import Path
from typing import Dict, List, Any

class MHWDatasetGenerator:
    def __init__(self):
        self.data = []  # Will store all generated QA pairs
        self.source_data_path = Path("source_data")
        
        # Load all data at initialization
        print("Loading data sources...")
        self.monster_data = self._load_monster_data()
        self.quest_data = self._load_quest_data()
        self.item_data = self._load_item_data()
        self.armor_data = self._load_armor_data()
        self.weapon_data = self._load_weapon_data()
        self.location_data = self._load_location_data()
        
        # Load templates
        self.templates = self._load_templates()

    def _load_monster_data(self) -> pd.DataFrame:
        """Load and preprocess monster data"""
        try:
            # Load base monster data
            monster_base = pd.read_csv(self.source_data_path / "monsters" / "monster_base.csv")
            monster_data = monster_base
            
            # Load weaknesses if available
            weakness_path = self.source_data_path / "monsters" / "monster_weaknesses.csv"
            if weakness_path.exists():
                monster_weakness = pd.read_csv(weakness_path)
                # Filter for normal form only
                monster_weakness = monster_weakness[monster_weakness['form'] == 'normal']
                monster_data = monster_data.merge(
                    monster_weakness,
                    left_on='name_en',
                    right_on='name_en',
                    how='left'
                )
            
            # Load rewards if available
            rewards_path = self.source_data_path / "monsters" / "monster_rewards.csv"
            if rewards_path.exists():
                monster_rewards = pd.read_csv(rewards_path)
                monster_data = monster_data.merge(
                    monster_rewards,
                    left_on='name_en',
                    right_on='monster_name',
                    how='left'
                )
            
            return monster_data
        except Exception as e:
            print(f"Error loading monster data: {e}")
            return pd.DataFrame()

    def _load_quest_data(self) -> pd.DataFrame:
        """Load and preprocess quest data"""
        try:
            quest_path = self.source_data_path / "quests" / "quest_base.csv"
            if not quest_path.exists():
                print(f"Warning: Quest data file not found at {quest_path}")
                return pd.DataFrame()
            quest_base = pd.read_csv(quest_path)
            # Ensure required columns exist
            if 'name' not in quest_base.columns and 'name_en' in quest_base.columns:
                quest_base = quest_base.rename(columns={'name_en': 'name'})
            return quest_base
        except Exception as e:
            print(f"Error loading quest data: {e}")
            return pd.DataFrame()

    def _load_item_data(self) -> pd.DataFrame:
        """Load and preprocess item data"""
        try:
            # Load base item data
            item_path = self.source_data_path / "items" / "item_base.csv"
            if not item_path.exists():
                print(f"Warning: Item data file not found at {item_path}")
                return pd.DataFrame()
            
            item_base = pd.read_csv(item_path)
            if 'name' not in item_base.columns and 'name_en' in item_base.columns:
                item_base = item_base.rename(columns={'name_en': 'name'})
            
            item_data = item_base
            
            # Try to load and merge combinations if they exist
            combinations_path = self.source_data_path / "items" / "item_combinations.csv"
            if combinations_path.exists():
                item_combinations = pd.read_csv(combinations_path)
                item_data = item_data.merge(item_combinations, on="id", how="left", suffixes=('', '_combo'))
            
            return item_data
        except Exception as e:
            print(f"Error loading item data: {e}")
            return pd.DataFrame()

    def _load_armor_data(self) -> pd.DataFrame:
        """Load and preprocess armor data"""
        try:
            # Load base armor data
            armor_path = self.source_data_path / "armors" / "armor_base.csv"
            if not armor_path.exists():
                print(f"Warning: Armor data file not found at {armor_path}")
                return pd.DataFrame()
            
            armor_base = pd.read_csv(armor_path)
            if 'name' not in armor_base.columns and 'name_en' in armor_base.columns:
                armor_base = armor_base.rename(columns={'name_en': 'name'})
            
            armor_data = armor_base
            
            # Try to load and merge additional armor data if files exist
            skills_path = self.source_data_path / "armors" / "armor_skills.csv"
            if skills_path.exists():
                armor_skills = pd.read_csv(skills_path)
                armor_data = armor_data.merge(armor_skills, on="id", how="left", suffixes=('', '_skills'))
            
            craft_path = self.source_data_path / "armors" / "armor_craft.csv"
            if craft_path.exists():
                armor_craft = pd.read_csv(craft_path)
                armor_data = armor_data.merge(armor_craft, on="id", how="left", suffixes=('', '_craft'))
            
            return armor_data
        except Exception as e:
            print(f"Error loading armor data: {e}")
            return pd.DataFrame()

    def _load_weapon_data(self) -> pd.DataFrame:
        """Load and preprocess weapon data"""
        try:
            # Load base weapon data
            weapon_path = self.source_data_path / "weapons" / "weapon_base.csv"
            if not weapon_path.exists():
                print(f"Warning: Weapon data file not found at {weapon_path}")
                return pd.DataFrame()
            
            weapon_base = pd.read_csv(weapon_path)
            if 'name' not in weapon_base.columns and 'name_en' in weapon_base.columns:
                weapon_base = weapon_base.rename(columns={'name_en': 'name'})
            
            weapon_data = weapon_base
            
            # Try to load and merge weapon craft data if it exists
            craft_path = self.source_data_path / "weapons" / "weapon_craft.csv"
            if craft_path.exists():
                weapon_craft = pd.read_csv(craft_path)
                weapon_data = weapon_data.merge(weapon_craft, on="id", how="left", suffixes=('', '_craft'))
            
            return weapon_data
        except Exception as e:
            print(f"Error loading weapon data: {e}")
            return pd.DataFrame()

    def _load_location_data(self) -> pd.DataFrame:
        """Load and preprocess location data"""
        try:
            # Load base location data
            location_path = self.source_data_path / "locations" / "location_base.csv"
            if not location_path.exists():
                print(f"Warning: Location data file not found at {location_path}")
                return pd.DataFrame()
            
            location_base = pd.read_csv(location_path)
            if 'name' not in location_base.columns and 'name_en' in location_base.columns:
                location_base = location_base.rename(columns={'name_en': 'name'})
            
            location_data = location_base
            
            # Try to load and merge additional location data if files exist
            camps_path = self.source_data_path / "locations" / "location_camps.csv"
            if camps_path.exists():
                location_camps = pd.read_csv(camps_path)
                location_data = location_data.merge(location_camps, on="id", how="left", suffixes=('', '_camps'))
            
            monsters_path = self.source_data_path / "locations" / "location_monsters.csv"
            if monsters_path.exists():
                location_monsters = pd.read_csv(monsters_path)
                location_data = location_data.merge(location_monsters, on="id", how="left", suffixes=('', '_monsters'))
            
            items_path = self.source_data_path / "locations" / "location_items.csv"
            if items_path.exists():
                location_items = pd.read_csv(items_path)
                location_data = location_data.merge(location_items, on="id", how="left", suffixes=('', '_items'))
            
            return location_data
        except Exception as e:
            print(f"Error loading location data: {e}")
            return pd.DataFrame()

    def _load_templates(self) -> Dict[str, Dict[str, str]]:
        """Load question/answer templates"""
        return {
            "monster_basic": {
                "system": "You are a Monster Hunter World expert who provides detailed information about monsters.",
                "question": "What kind of monster is {name}?",
                "answer": "{name} is a {species} class monster. It is classified as a {size} monster and is {elder_dragon_text}."
            },
            "monster_weakness": {
                "system": "You are a Monster Hunter World expert who provides detailed information about monsters.",
                "question": "What are {name}'s weaknesses?",
                "answer": "{name} is most vulnerable to {element1} (★★★) and {element2} (★★) attacks. For status effects, it's particularly susceptible to {status1}."
            },
            "monster_rewards": {
                "system": "You are a Monster Hunter World expert who provides detailed information about monsters.",
                "question": "What materials can I get from {name}?",
                "answer": "From {name}, you can obtain:\n- {material1} (Common reward, {drop_rate1}%)\n- {material2} (Rare reward, {drop_rate2}%)\n- {material3} (Break reward from {body_part})\n{rare_material_text}"
            },
            "quest_info": {
                "system": "You are a Monster Hunter World quest advisor.",
                "question": "Tell me about the quest '{name}'",
                "answer": "'{name}' is a {rank}★ {quest_type} quest. Location: {location}. Target: {target}. Reward: {zenny}z and {reward_items}. Time limit: {time_limit} minutes. {conditions_text}"
            },
            "quest_requirements": {
                "system": "You are a Monster Hunter World quest advisor.",
                "question": "What do I need to do to unlock '{name}'?",
                "answer": "To unlock '{name}', you need:\n- Hunter Rank {required_rank} or higher\n{prerequisites_text}\n{special_requirement_text}"
            },
            "item_info": {
                "system": "You are a Monster Hunter World item expert.",
                "question": "What is {name} used for?",
                "answer": "{name} is a {rarity}-star {item_type}. {description} {obtain_method}"
            },
            "crafting_info": {
                "system": "You are a Monster Hunter World crafting expert.",
                "question": "How do I craft {name}?",
                "answer": "To craft {name}, you need:\n{materials_list}\nThis recipe produces {yield} {name}{alternative_recipe_text}"
            },
            "armor_stats": {
                "system": "You are a Monster Hunter World equipment expert.",
                "question": "What are the stats of {name}?",
                "answer": "{name} ({armor_type}) has:\n- Defense: {defense}\n- Resistances:\n  * Fire: {fire_res}\n  * Water: {water_res}\n  * Thunder: {thunder_res}\n  * Ice: {ice_res}\n  * Dragon: {dragon_res}\nSkills:\n{skills_list}"
            },
            "armor_set": {
                "system": "You are a Monster Hunter World equipment expert.",
                "question": "Tell me about the {name} armor set",
                "answer": "The {name} set consists of:\n{pieces_list}\nSet Bonus: {bonus_name} ({bonus_description})\nRequired pieces for bonus: {pieces_required}"
            },
            "weapon_stats": {
                "system": "You are a Monster Hunter World weapon expert.",
                "question": "What are the stats of {name}?",
                "answer": "{name} ({weapon_type}):\n- Attack: {attack}\n{element_text}\n{affinity_text}\n{sharpness_text}\n{bowgun_text}\n{bow_text}\nSlots: {slot_configuration}"
            },
            "weapon_crafting": {
                "system": "You are a Monster Hunter World weapon expert.",
                "question": "How do I craft {name}?",
                "answer": "To craft {name}, you need:\n{materials_list}\nCost: {zenny}z\n{prerequisite_text}"
            },
            "location_info": {
                "system": "You are a Monster Hunter World location expert.",
                "question": "What can I find in {name}?",
                "answer": "{name} features:\nMonsters:\n{monsters_list}\nGathering Points:\n{gathering_points}\nCamps: {camps}"
            }
        }

    def _create_qa_pair(self, template_key: str, format_dict: Dict[str, Any]) -> Dict[str, List[Dict[str, str]]]:
        """Create a QA pair using a template and format dictionary"""
        template = self.templates[template_key]
        return {
            "messages": [
                {"role": "system", "content": template["system"]},
                {"role": "user", "content": template["question"].format(**format_dict)},
                {"role": "assistant", "content": template["answer"].format(**format_dict)}
            ]
        }

    def generate_monster_questions(self):
        """Generate all monster-related questions"""
        with tqdm(total=len(self.monster_data), desc="Generating monster questions") as pbar:
            for _, monster in self.monster_data.iterrows():
                # Prepare format dictionary
                monster_dict = {
                    'name': monster['name_en'],
                    'species': monster.get('ecology_en', 'Unknown'),
                    'size': monster['size'],
                    'elder_dragon_text': "an Elder Dragon" if monster.get('ecology_en') == 'Elder Dragon' else f"part of the {monster.get('ecology_en', 'Unknown')} category" if monster.get('ecology_en') else "an unknown type"
                }
                
                # Generate basic info question
                self.data.append(self._create_qa_pair("monster_basic", monster_dict))
                
                # Add weakness information if available
                if 'fire' in monster:
                    # Find top two elemental weaknesses
                    elements = {'fire': monster['fire'], 'water': monster['water'], 
                              'thunder': monster['thunder'], 'ice': monster['ice'], 
                              'dragon': monster['dragon']}
                    sorted_elements = sorted(elements.items(), key=lambda x: x[1], reverse=True)
                    
                    # Find highest status effect
                    status_effects = {'poison': monster['poison'], 'sleep': monster['sleep'],
                                    'paralysis': monster['paralysis'], 'blast': monster['blast'],
                                    'stun': monster['stun']}
                    top_status = max(status_effects.items(), key=lambda x: x[1])
                    
                    weakness_dict = {
                        'name': monster['name_en'],
                        'element1': sorted_elements[0][0],
                        'element2': sorted_elements[1][0],
                        'status1': top_status[0]
                    }
                    self.data.append(self._create_qa_pair("monster_weakness", weakness_dict))
                
                # Add rewards information if available
                if 'rewards' in monster:
                    rewards_dict = {
                        'name': monster['name_en'],
                        'material1': monster.get('common_reward', 'Various materials'),
                        'drop_rate1': monster.get('common_rate', '0'),
                        'material2': monster.get('rare_reward', 'Rare materials'),
                        'drop_rate2': monster.get('rare_rate', '0'),
                        'material3': monster.get('break_reward', 'Break part rewards'),
                        'body_part': monster.get('break_part', 'various parts'),
                        'rare_material_text': ''
                    }
                    if monster.get('rare_material'):
                        rewards_dict['rare_material_text'] = f"The {monster['rare_material']} has a very low drop rate of {monster.get('rare_drop_rate', '0')}% and is best obtained through investigations."
                    self.data.append(self._create_qa_pair("monster_rewards", rewards_dict))
                
                pbar.update(1)

    def generate_quest_questions(self):
        """Generate all quest-related questions"""
        with tqdm(total=len(self.quest_data), desc="Generating quest questions") as pbar:
            for _, quest in self.quest_data.iterrows():
                quest_dict = quest.to_dict()

                
                # Format quest data to match templates
                formatted_quest = {
                    'name': quest_dict['name'],
                    'rank': quest_dict['stars'],  # Use stars for rank display
                    'quest_type': quest_dict['quest_type'],
                    'location': quest_dict['location_en'],
                    'target': 'Various monsters',  # Default target
                    'zenny': quest_dict['zenny'],
                    'reward_items': 'Various items',  # Default rewards
                    'time_limit': '50',  # Default time limit
                    'conditions_text': '',  # No conditions in base CSV
                    'required_rank': quest_dict['rank'],  # Use rank (LR/HR) for requirements
                    'prerequisites_text': '',  # No prerequisites in base CSV
                    'special_requirement_text': '',  # No special requirements in base CSV
                    'category': quest_dict['category']
                }
                
                # Add category-specific text
                if formatted_quest['category'] == 'assigned':
                    formatted_quest['special_requirement_text'] = '- This is a story progression quest'
                elif formatted_quest['category'] == 'optional':
                    formatted_quest['special_requirement_text'] = '- This is an optional quest'
                
                # Generate quest info question
                self.data.append(self._create_qa_pair("quest_info", formatted_quest))
                
                # Generate requirements question
                self.data.append(self._create_qa_pair("quest_requirements", formatted_quest))
                
                pbar.update(1)

    def generate_item_questions(self):
        """Generate all item-related questions"""
        with tqdm(total=len(self.item_data), desc="Generating item questions") as pbar:
            for _, item in self.item_data.iterrows():
                item_dict = item.to_dict()
                
                # Format item data
                formatted_item = {
                    'name': item_dict['name'],
                    'rarity': item_dict['rarity'],
                    'item_type': item_dict.get('category', 'consumable'),
                    'description': f"It can be carried up to {item_dict['carry_limit']} at a time.",
                    'obtain_method': ''
                }
                
                # Add price information if available
                if item_dict.get('buy_price'):
                    formatted_item['obtain_method'] = f"It can be purchased for {item_dict['buy_price']} zenny."
                elif item_dict.get('points'):
                    formatted_item['obtain_method'] = f"It can be obtained for {item_dict['points']} resource points."
                
                # Generate item info question
                self.data.append(self._create_qa_pair("item_info", formatted_item))
                
                pbar.update(1)

    def generate_armor_questions(self):
        """Generate all armor-related questions"""
        with tqdm(total=len(self.armor_data), desc="Generating armor questions") as pbar:
            for _, armor in self.armor_data.iterrows():
                armor_dict = armor.to_dict()

                
                # Format armor data
                formatted_armor = {
                    'name': armor_dict['name'],
                    'armor_type': armor_dict['type'],
                    'defense': armor_dict['defense_base'],
                    'fire_res': armor_dict['defense_fire'],
                    'water_res': armor_dict['defense_water'],
                    'thunder_res': armor_dict['defense_thunder'],
                    'ice_res': armor_dict['defense_ice'],
                    'dragon_res': armor_dict['defense_dragon'],
                    'skills_list': 'No skills available'  # Default if no skills data
                }
                
                # Add skills if available
                if 'skills' in armor_dict and 'skill_levels' in armor_dict:
                    formatted_armor["skills_list"] = "\n".join([f"- {skill}: Level {level}" 
                        for skill, level in zip(armor_dict['skills'].split(','), 
                                              armor_dict['skill_levels'].split(','))])
                
                # Generate armor stats question
                self.data.append(self._create_qa_pair("armor_stats", formatted_armor))
                
                # Generate armor set question if part of a set
                if armor_dict.get('set_name'):
                    formatted_armor["pieces_list"] = "\n".join([f"- {piece}" for piece in armor_dict['set_pieces'].split(',')])
                    formatted_armor["bonus_name"] = armor_dict.get('set_bonus_name', 'None')
                    formatted_armor["bonus_description"] = armor_dict.get('set_bonus_description', 'No bonus')
                    formatted_armor["pieces_required"] = armor_dict.get('set_pieces_required', '3')
                    self.data.append(self._create_qa_pair("armor_set", formatted_armor))
                
                pbar.update(1)

    def generate_weapon_questions(self):
        """Generate all weapon-related questions"""
        with tqdm(total=len(self.weapon_data), desc="Generating weapon questions") as pbar:
            for _, weapon in self.weapon_data.iterrows():
                weapon_dict = weapon.to_dict()
                
                # Format weapon data
                formatted_weapon = {
                    'name': weapon_dict['name_en'],
                    'weapon_type': weapon_dict['weapon_type'].replace('-', ' ').title(),
                    'attack': weapon_dict['attack'],
                    'element_text': '',
                    'affinity_text': '',
                    'slot_configuration': f"{weapon_dict['slot_1']}-{weapon_dict['slot_2']}-{weapon_dict['slot_3']}",
                    'sharpness_text': '',  # No sharpness in base data
                    'bowgun_text': '',  # Ammo config would go here if present
                    'bow_text': ''  # Coating info would go here if present
                }
                
                # Add element information if available
                if weapon_dict.get('element1'):
                    formatted_weapon['element_text'] = f"- Element: {weapon_dict['element1']} {weapon_dict['element1_attack']}"
                    if weapon_dict.get('element2'):
                        formatted_weapon['element_text'] += f"\n- Secondary Element: {weapon_dict['element2']} {weapon_dict['element2_attack']}"
                    if weapon_dict.get('element_hidden'):
                        formatted_weapon['element_text'] += " (Hidden)"
                
                # Add affinity if non-zero
                if weapon_dict.get('affinity', 0) != 0:
                    formatted_weapon['affinity_text'] = f"- Affinity: {weapon_dict['affinity']}%"
                
                # Add special weapon properties
                if weapon_dict.get('phial'):
                    formatted_weapon['element_text'] += f"\n- Phial Type: {weapon_dict['phial']}"
                    if weapon_dict.get('phial_power'):
                        formatted_weapon['element_text'] += f" ({weapon_dict['phial_power']})"
                
                if weapon_dict.get('shelling'):
                    formatted_weapon['sharpness_text'] = f"- Shelling Type: {weapon_dict['shelling']} Lv{weapon_dict['shelling_level']}"
                
                if weapon_dict.get('notes'):
                    formatted_weapon['bow_text'] = f"- Notes: {weapon_dict['notes']}"
                
                if weapon_dict.get('ammo_config'):
                    formatted_weapon['bowgun_text'] = f"- Ammo Configuration: {weapon_dict['ammo_config']}"
                
                # Generate weapon stats question
                self.data.append(self._create_qa_pair("weapon_stats", formatted_weapon))
                
                # Format crafting information if available
                if weapon_dict.get('previous_en'):
                    formatted_weapon['prerequisite_text'] = f"Requires previous weapon: {weapon_dict['previous_en']}"
                    formatted_weapon['materials_list'] = "Materials information not available in base data"
                    formatted_weapon['zenny'] = "0"  # Cost not available in base data
                    self.data.append(self._create_qa_pair("weapon_crafting", formatted_weapon))
                
                pbar.update(1)

    def generate_dataset(self):
        """Generate complete dataset"""
        print("Generating dataset...")
        with tqdm(total=6, desc="Overall progress") as pbar:
            self.generate_monster_questions()
            pbar.update(1)
            self.generate_quest_questions()
            pbar.update(1)
            self.generate_item_questions()
            pbar.update(1)
            self.generate_armor_questions()
            pbar.update(1)
            self.generate_weapon_questions()
            pbar.update(1)
            self.generate_location_questions()
            pbar.update(1)
            
        return self.save_dataset()

    def generate_location_questions(self):
        """Generate all location-related questions"""
        with tqdm(total=len(self.location_data), desc="Generating location questions") as pbar:
            for _, location in self.location_data.iterrows():
                location_dict = location.to_dict()
                
                # Format location data
                formatted_location = {
                    'name': location_dict['name_en'],
                    'monsters_list': 'Various monsters can be found here',  # Default text
                    'gathering_points': 'Various gathering points available',  # Default text
                    'camps': 'Multiple camps available'  # Default text
                }
                
                # Generate location info question
                self.data.append(self._create_qa_pair("location_info", formatted_location))
                
                pbar.update(1)

    def save_dataset(self) -> tuple[str, str]:
        """Save generated QA pairs to training and validation JSONL files"""
        import random
        
        # Shuffle the data
        random.shuffle(self.data)
        
        # Split into training (90%) and validation (10%) sets
        split_idx = int(len(self.data) * 0.9)
        train_data = self.data[:split_idx]
        val_data = self.data[split_idx:]
        
        # Save training data
        train_file = "mhw_train.jsonl"
        with open(train_file, 'w', encoding='utf-8') as f:
            for qa_pair in train_data:
                f.write(json.dumps(qa_pair, ensure_ascii=False) + '\n')
        
        # Save validation data
        val_file = "mhw_val.jsonl"
        with open(val_file, 'w', encoding='utf-8') as f:
            for qa_pair in val_data:
                f.write(json.dumps(qa_pair, ensure_ascii=False) + '\n')
        
        print(f"\nDataset split and saved:")
        print(f"Training set ({len(train_data)} examples): {train_file}")
        print(f"Validation set ({len(val_data)} examples): {val_file}")
        print(f"Total generated: {len(self.data)} question-answer pairs")
        
        return train_file, val_file

def main():
    generator = MHWDatasetGenerator()
    generator.generate_dataset()

if __name__ == "__main__":
    main()
