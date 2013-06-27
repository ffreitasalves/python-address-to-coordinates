import urllib
import simplejson

def coordinates(address):
    url = 'http://maps.google.com/maps/api/geocode/json?address=%s&sensor=false' % address
    coord = simplejson.load(
        urllib.urlopen(url)
    )

    if coord['status'] == 'OK':
        return {
            'lat': coord['results'][0]['geometry']['location']['lat'],
            'lng': coord['results'][0]['geometry']['location']['lng'],
        }
    else:
        return {
            'lat': '',
            'lng': '',
            }

def xlsx_coordinates(input_file, sheet_name,address_column, output_file, ignore_first_row = True):
    """
    Read the xlsx input_file, and add two new columns in the beginning of it with latitude and longitude
    Input file must be a xls* file
    """

    wb_read = load_workbook(input_file)
    sh = wb_read.get_sheet_by_name(sheet_name)
    if ignore_first_row:
        #Ignore first line of the file
        first = 1
    else:
        first = 0

    out = []
    for row in sh.rows[first:]:
        coord = coordinates(row[address_column].value)
        new_row = [coord['lat'],coord['lng']]
        for c in row:
            new_row.append(c.value)
        out.append(new_row)

    wb_write = Workbook(optimized_write=True)
    sheet = wb_write.create_sheet(0,sheet_name)

    for row in out:
        sheet.append(row)

    wb_write.save(output_file)
