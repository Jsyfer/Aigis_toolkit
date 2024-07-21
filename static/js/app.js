import * as api from "./api.js";

// window.onload = function () {
//     table.setData("/units");
// };

const cellEditor = (cell) => {
    api.update_by_id(cell)
}


//create Tabulator on DOM element with id "example-table"
var table = new Tabulator("#example-table", {
    height: 1000,
    placeholder: "No Data Set",
    pagination: "local",
    paginationSize: 30,
    paginationSizeSelector: [30, 50, 100],
    ajaxURL: "/units",
    index: "id",
    columns: [ //Define Table Columns
        { title: "ID", field: "id", width: 50 },
        {
            title: "画像", field: "icon", width: 70, formatter: "image", hozAlign: "center", formatterParams: {
                height: "50px",
                width: "50px",
            }
        },
        { title: "名前", field: "unit_name", headerFilter: "input" },
        {
            title: "リア",
            field: "rare",
            width: 70,
            headerFilter: true, headerFilter: "list",
            headerFilterParams: { valuesLookup: true, clearable: true }
        },
        { title: "所持済", field: "owned", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true }, cellEdited: cellEditor },
        { title: "覚醒済", field: "is_awakening", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true }, cellEdited: cellEditor },
        { title: "交流クエスト", field: "has_extra_story", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true }, cellEdited: cellEditor },
        { title: "育成済", field: "all_complete", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true }, cellEdited: cellEditor },
    ]
});

