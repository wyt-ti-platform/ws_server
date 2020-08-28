import xml.etree.ElementTree as ET


class MyXML:
    def __init__(self, xml_file):
        self._xml_file = xml_file
        self._tree = ET.parse(xml_file)
        self._root = self._tree.getroot()

    def update_node(self, path, match_kv, update_kv):
        nodes = self._root.findall(path)
        for node in nodes:
            if MyXML._is_matched(node, match_kv):
                MyXML._update_node_attr(node, update_kv)

    def save(self, dest_file=None):
        xml_file = self._xml_file if dest_file is None else dest_file
        self._tree.write(xml_file, encoding='utf-8', xml_declaration=True)

    @staticmethod
    def update_xml(xml_file, path, match_kv, update_kv):
        my_xml = MyXML(xml_file)
        my_xml.update_node(path, match_kv, update_kv)
        my_xml.save()
        # tree = ET.parse(xml_file)
        # root = tree.getroot()
        # nodes = root.findall(path)
        # for node in nodes:
        #     if MyXML._is_matched(node, match_kv):
        #         MyXML._update_node_attr(node, update_kv)
        # tree.write(xml_file, encoding='utf-8', xml_declaration=True)

    @staticmethod
    def _is_matched(node, match_kv):
        for key in match_kv:
            if node.get(key) != match_kv.get(key):
                return False
        return True

    @staticmethod
    def _update_node_attr(node, update_kv):
        for key in update_kv:
            node.set(key, update_kv.get(key))


