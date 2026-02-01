from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHandleMenu(Action):
    """Handle menu selection based on menu_number entity"""

    def name(self) -> Text:
        return "action_handle_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get menu_number entity
        menu_number = next(tracker.get_latest_entity_values("menu_number"), None)
        
        # If no entity found, ask user to select
        if not menu_number:
            dispatcher.utter_message(response="utter_fallback")
            return []
        
        # Normalize menu number (handle synonyms)
        menu_map = {
            "1": "utter_apa_itu_stroke",
            "satu": "utter_apa_itu_stroke",
            "pertama": "utter_apa_itu_stroke",
            "2": "utter_gejala_stroke",
            "dua": "utter_gejala_stroke",
            "kedua": "utter_gejala_stroke",
            "3": "utter_penyebab_stroke",
            "tiga": "utter_penyebab_stroke",
            "ketiga": "utter_penyebab_stroke",
            "4": "utter_pencegahan_stroke",
            "empat": "utter_pencegahan_stroke",
            "keempat": "utter_pencegahan_stroke",
            "5": "utter_penanganan_stroke",
            "lima": "utter_penanganan_stroke",
            "kelima": "utter_penanganan_stroke",
        }
        
        # Get response based on menu number
        response = menu_map.get(str(menu_number).lower())
        
        if response:
            dispatcher.utter_message(response=response)
        else:
            dispatcher.utter_message(response="utter_fallback")
        
        return []