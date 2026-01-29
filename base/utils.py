def add_to_bag(request, item_id):
    item_id = str(item_id)
    bag_dict = request.session.get('bag', {})
    bag_dict[item_id] = bag_dict.get(item_id, 0) + 1
    request.session['bag'] = bag_dict
    request.session.modified = True






import requests

def get_random_activity():
    url = 'https://www.boredapi.com/api/activity'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['activity']
    else:
        return 'Something interesting'

