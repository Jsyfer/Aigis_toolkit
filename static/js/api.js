const style_ok_response = () => {
    document.querySelector("#layout_main_panel_bottom").style.backgroundColor = '#deffbd';
    setTimeout(function () {
        document.querySelector("#layout_main_panel_bottom").style.backgroundColor = '#fcfcfc';
    }, 1000);
}

const style_error_response = () => {
    document.querySelector("#layout_main_panel_bottom").style.backgroundColor = '#ffc4c4';
    setTimeout(function () {
        document.querySelector("#layout_main_panel_bottom").style.backgroundColor = '#fcfcfc';
    }, 1000);
}

export const get_all_unit = () => {
    fetch('/units')
        .then(response => response.json())
        .then(data => {
            var tabledata = data;
            //create Tabulator on DOM element with id "example-table"
            var table = new Tabulator("#example-table", {
                height: "100%",// set height of table (in CSS or here), this enables the Virtual DOM and improves render speed dramatically (can be any valid css height value)
                data: tabledata, //assign data to table
                layout: "fitColumns", //fit columns to width of table (optional)
                columns: [ //Define Table Columns
                    { title: "ID", field: "id", width: 50, headerFilter: "number" },
                    {
                        title: "画像", field: "icon", width: 70, formatter: "image", hozAlign: "center", formatterParams: {
                            height: "50px",
                            width: "50px",
                        }
                    },
                    { title: "名前", field: "unit_name", editor: "input", headerFilter: "input" },
                    {
                        title: "リア",
                        field: "rare",
                        width: 70,
                        editor: "list",
                        editorParams: { autocomplete: "true", listOnEmpty: true, valuesLookup: true },
                        headerFilter: true, headerFilter: "list",
                        headerFilterParams: { valuesLookup: true, clearable: true }
                    },
                    { title: "所持済", field: "owned", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true } },
                    { title: "覚醒済", field: "is_awakening", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true } },
                    { title: "交流クエスト", field: "has_extra_story", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true } },
                    { title: "交流クエストクリア", field: "complete_extra_story", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true } },
                    { title: "育成済", field: "all_complete", editor: true, formatter: "tickCross", headerFilter: "tickCross", headerFilterParams: { "tristate": true } },
                ],
            });
        })
        .catch((error) => {
            document.querySelector("#layout_main_panel_bottom").innerHTML = "Error:" + error
            style_error_response()
        });
}

