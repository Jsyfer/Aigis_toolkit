import * as api from "./api.js";

// window.onload = function () {
//     table.setData("/units");
// };

const cellEditor = (cell) => {
    api.update_by_id(cell)
}

const cellClick = (e, cell) => {
    window.open("https://wikiwiki.jp" + cell.getRow().getData().info_url, "_blank");
}


//create Tabulator on DOM element with id "example-table"
var table = new Tabulator("#example-table", {
    placeholder: "No Data Set",
    pagination: "local",
    paginationSize: 100,
    paginationSizeSelector: [30, 50, 100],
    ajaxURL: "/units",
    index: "id",
    rowHeader: { formatter: "rownum", headerSort: false, hozAlign: "center", resizable: false, frozen: true },
    columns: [ //Define Table Columns
        { title: "ID", field: "id", width: 60 },
        {
            title: "画像", field: "icon", width: 70, formatter: "image", hozAlign: "center", formatterParams: {
                height: "50px",
                width: "50px",
            }
        },
        { title: "名前", field: "unit_name", headerFilter: "input", cellClick: cellClick },
        {
            title: "リア",
            field: "rare",
            width: 70,
            headerFilter: "list",
            headerFilterParams: { valuesLookup: true, clearable: true }
        },
        { title: "入手方法", field: "obtain_method", headerFilter: "list", headerFilterParams: { valuesLookup: true, clearable: true } },
        { title: "所属", field: "property_belong", headerFilter: "list", headerFilterParams: { valuesLookup: true, clearable: true } },
        { title: "種族", field: "property_race", headerFilter: "list", headerFilterParams: { valuesLookup: true, clearable: true } },
        { title: "特性", field: "property_speciality", headerFilter: "list", headerFilterParams: { valuesLookup: true, clearable: true } },
        { title: "季節", field: "property_season", headerFilter: "list", headerFilterParams: { valuesLookup: true, clearable: true } },
        { title: "適性", field: "property_qualification", headerFilter: "list", headerFilterParams: { valuesLookup: true, clearable: true } },
        { title: "コラボ", field: "property_collaboration", headerFilter: "list", headerFilterParams: { valuesLookup: true, clearable: true } },
        { title: "遠近", field: "property_distance", headerFilter: "list", headerFilterParams: { valuesLookup: true, clearable: true } },
        { title: "性別", field: "property_sex", headerFilter: "list", headerFilterParams: { valuesLookup: true, clearable: true } },
        { title: "覚醒素材", field: "awakening_material", headerFilter: "input", headerFilterParams: { valuesLookup: true, clearable: true } },
        { title: "所持済", field: "owned", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true }, cellEdited: cellEditor },
        { title: "覚醒済", field: "is_awakening", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true }, cellEdited: cellEditor },
        { title: "交流クエスト", field: "has_extra_story", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true }, cellEdited: cellEditor },
        { title: "育成済", field: "all_complete", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true }, cellEdited: cellEditor },
    ]
});

document.getElementById('clearFilter').onclick = () => {
    table.clearHeaderFilter();
}