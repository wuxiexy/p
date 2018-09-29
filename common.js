document.body.style.opacity = 0;
window.onload = function () {
    var doc = document
        , t = doc.title
        , container = doc.getElementById('sds1_resultTable')
        , con = container.innerHTML
        , docBody = doc.body, trs, len, i = 1, td, area, price, currentTd
        , areatotal = 0
        , pricetotal = 0
        , total = 0
        , tr = doc.createElement('tr')
    ;

    doc.head.innerHTML = '';
    doc.title = t;
    doc.form1.remove();
    doc.body.appendChild(container);
    container = doc.getElementById('sds1_resultTable');
    docBody.style.opacity = 1;

    trs = container.getElementsByTagName('tr');
    len = trs.length;

    // 添加单价
    td = doc.createElement('td');
    td.innerHTML = '当日平均单价（元）';
    trs[0].appendChild(td);

    for (; i < len; i++) {
        current = trs[i];
        currentTd = current.getElementsByTagName('td');
        price = +currentTd[3].innerHTML;        // 总金额
        area = +currentTd[2].innerHTML;         // 总面积

        areatotal += area;
        pricetotal += price;

        td = doc.createElement('td');
        if (price == 0 || area == 0) {
            td.innerHTML = 0;
        } else {
            td.innerHTML = (price / area * 10000).toFixed(2) + ' 元';
        }
        current.appendChild(td);
    }
    window.console.clear();
    total = (pricetotal / areatotal * 10000).toFixed(2) + ' 元'
    tr.innerHTML = '<td>-</td><td>-</td><td>'+areatotal.toFixed(2)+' ㎡</td><td>'+pricetotal.toFixed(2)+' 万</td><td>平均 '+total+'</td>';
    container.getElementsByTagName('tbody')[0].appendChild(tr);
}