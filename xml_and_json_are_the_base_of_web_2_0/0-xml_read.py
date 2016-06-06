from xml.dom import minidom

doc = minidom.parse("catalogs.xml")

f = open('0-xml_read.txt', 'w')

i =1

catalog = doc.getElementsByTagName("catalog")

# How many catalog_item elements in the XML?
catalog_items = doc.getElementsByTagName("catalog_item")
f.write(str(i)+') '+str(len(catalog_items))+'\n')
i += 1

#How many size elements in catalog_item where the gender="Women's" in the XML?
for catalog_item in catalog_items:
    if catalog_item.getAttribute("gender") == "Women's":
        sizes = catalog_item.getElementsByTagName('size')
        f.write(str(i)+') '+str(len(sizes))+'\n')
        i += 1
#What's the value of the first color_swatch for a Women's Medium item
        for size in sizes:
            if size.getAttribute("description") == "Medium":
                color = size.getElementsByTagName('color_swatch')[0]
                f.write(str(i)+') '+color.firstChild.nodeValue+'\n')
                i += 1

#What's the price of the Men's item
for catalog_item in catalog_items:
    if catalog_item.getAttribute("gender") == "Men's":
        price = catalog_item.getElementsByTagName('price')[0].firstChild.nodeValue
        f.write(str(i)+') '+str(price)+'\n')
        i += 1
#How many different unique image value are present in the XML?
images = doc.getElementsByTagName("color_swatch")
imagevalues = []
for image in images:
    imagevalues.append(image.getAttribute("image"))
f.write(str(i)+') '+str(len(list(set(imagevalues))))+'\n')
i += 1

#check if the first node is an element node
def get_firstChild(n) :
    y = n.firstChild
    while y.nodeType != 1:
        y = y.nextSibling
    return y

#What's the name of the first children of a catalog_item element?
f.write(str(i)+') '+get_firstChild(catalog_items[0]).nodeName+'\n')
i += 1

sizes = doc.getElementsByTagName("size")
#What's the name of the first children of a size element?
f.write(str(i)+') '+get_firstChild(sizes[0]).nodeName+'\n')
f.close()

