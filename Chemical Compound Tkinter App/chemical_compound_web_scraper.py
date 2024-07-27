import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
from io import BytesIO

class UnableToFindCompoundError(Exception):
    pass

def check_response(response: requests.models.Response):
    if response.status_code != 200:
        raise UnableToFindCompoundError

def get_cid(compound_name: str) -> str:
    compound_name = compound_name.strip()
    encoded_name = compound_name.replace(' ', '%20')
    url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{encoded_name}/cids/TXT'
    cid_response = requests.get(url)
    check_response(cid_response)
    cid = BeautifulSoup(cid_response.text, 'html.parser')
    return str(cid)

def get_compound_info(cid: str, url_property: str) -> "ImageTk.PhotoImage | bs4.BeautifulSoup":
    if url_property == 'Image':
        url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid.lstrip().rstrip()}/PNG'
        structure_image_response = requests.get(url)
        structure_image_data = BytesIO(structure_image_response.content)
        structure_image = Image.open(structure_image_data)
        structure_image = structure_image.resize((275, 275), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(structure_image)
    else:
        url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid.lstrip().rstrip()}/property/{url_property}/TXT'
    
    response = requests.get(url)
    property = BeautifulSoup(response.text, 'html.parser')
    return property

def execute(compound_name: str, cid: str):
    compound_name = compound_name.strip().title()
    #print(f'Name: {compound_name}')

    molecular_formula = get_compound_info(cid, 'MolecularFormula')
    #print(f'Molecular Formula: {molecular_formula}', end='')

    molecular_weight = get_compound_info(cid, 'MolecularWeight')
    #print(f'Molecular Weight: {molecular_weight}', end='')

    structure_image = get_compound_info(cid, 'Image')
    #print('Image retrieved')
    
    return compound_name, molecular_formula, molecular_weight, structure_image
    