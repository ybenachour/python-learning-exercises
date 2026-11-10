"""Practice parsing web data formats using local example strings."""
import json
import xml.etree.ElementTree as ET


def parse_json_record(payload: str) -> dict:
    value = json.loads(payload)
    if not isinstance(value, dict):
        raise ValueError("expected a JSON object")
    return value


def parse_xml_values(xml_text: str) -> list[str]:
    root = ET.fromstring(xml_text)
    return [item.text or "" for item in root.findall(".//item")]


if __name__ == "__main__":
    print(parse_json_record('{"topic":"Python","completed":true}'))
    print(parse_xml_values("<items><item>JSON</item><item>XML</item></items>"))
