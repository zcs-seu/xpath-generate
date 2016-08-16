#encoding=utf-8
def generate_xpath(child):
    nodes=[];
    xpath="//"
    curnode=parent=child;
    try:
        attrs0=child.attrs;
        nodes.append(curnode);
    except:
        parent=child.findParent();
        curnode=parent;
        nodes.append(curnode);
    if curnode.name=='a' or curnode.name=='A' or curnode.name=='img':
        parent=curnode.findParent();
        curnode=parent;
        nodes.append(curnode);
        nodenum=nodes.__len__();
        for j in range(0,nodenum):
            i=nodenum-1-j;
            curnode=nodes[i];
            try:
                xpath=xpath+curnode.name;
            except:
                return xpath; #2016.06.07
            try:
                attrs=curnode.attrs;
            except:
                curnode=curnode.findParent();
                attrs=curnode.attrs;
            attrnames=attrs.keys();
            length=attrs.__len__();length=length-1;
            if length>=0 and (attrnames.__contains__('id')==True or attrnames.__contains__('class')==True):
                xpath=xpath+"[";
                if attrnames.__contains__('id')==True:
                    xpath=xpath+"@id='"+attrs.__getitem__("id")+"']/";
                    continue
                if attrnames.__contains__('class')==True:
                    #xpath=xpath+"@class='"+attrs.__getitem__("class")[0]+"']/";
                    try:
                        #此时，beautifulsoup获得的class为一个字符串— —2016.06.07
                        xpath=xpath+"@class='"+attrs.__getitem__("class")+"']/";
                    except:
                        resultset=attrs.__getitem__("class");
                        cur="";
                        for r1 in resultset:#2016.06.07
                            if r1==None:r1="";
                            cur=cur+r1+" ";
                        xpath=xpath+"@class='"+cur.strip()+"']/";
                    continue
            if length==0:
                attrname=attrnames[0];
                try:
                    #此时，beautifulsoup获得的attrname属性值为一个字符串— —2016.06.07
                    xpath=xpath+"[@"+attrname+"='"+attrs.__getitem__(attrname)+"']/";
                except:
                    print "attrs has no attrname"
                continue
            else:
                xpath=xpath+"/";
                continue
        xpath=xpath+"text()";
    else:
        nodenum=nodes.__len__();
        for j in range(0,nodenum):
            i=nodenum-1-j;
            try:
                curnode=nodes[i];
            except:
                print 'list out of range,index is %d' % i
            try:
                xpath=xpath+curnode.name;
            except:
                return xpath;
            try:
                attrs=curnode.attrs;
            except:
                curnode=curnode.findParent();
                attrs=curnode.attrs;
            attrnames=attrs.keys();
            length=attrs.__len__();length=length-1;
            if length>=0 and (attrnames.__contains__('id')==True or attrnames.__contains__('class')==True):
                xpath=xpath+"[";
                if attrnames.__contains__('id')==True:
                    xpath=xpath+"@id='"+attrs.__getitem__("id")+"']/";
                    continue;
                if attrnames.__contains__('class')==True:
                    try:
                        #此时，beautifulsoup获得的class属性值为一个字符串— —2016.06.07
                        xpath=xpath+"@class='"+attrs.__getitem__("class")+"']/";
                    except:
                        resultset=attrs.__getitem__("class");
                        cur="";
                        for r1 in resultset:#2016.06.07
                            if r1==None:r1="";
                            cur=cur+r1+" ";
                        xpath=xpath+"@class='"+cur.strip()+"']/";
                    continue;
            if length==0:
                attrname=attrnames[0];
                try:
                    #此时，beautifulsoup获得的class属性值为一个字符串— —2016.06.07
                    xpath=xpath+"[@"+attrname+"='"+attrs.__getitem__(attrname)+"']/";
                except:
                    print "attrs has no attrname"
                #xpath=xpath+"[@"+attrname+"='"+attrs.__getitem__(attrname)+"']/";
                continue;
            else:
                xpath=xpath+"/";
                continue;
        xpath=xpath+"text()";
    return xpath;