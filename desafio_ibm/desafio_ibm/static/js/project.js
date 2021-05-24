/* Project specific Javascript goes here. */

//Chosen select
$(".chzn-select").chosen(
                  {
                   no_results_text: "Nenhum resultado encontrado para: ",
                   search_contains: true,
                   display_disabled_options: false,
                   display_selected_options: false,
                   allow_single_deselect: true,
                  });

function addHidden(form, key, value) {
  // Create a hidden input element, and append it to the form:
  $('<input>').attr({type: 'hidden',
                     id: key,
                     name: key,
                     value: value
                    }).appendTo(form);

}


function highlight(term, element){
    // Highlight
    options = {'diacritics': true,
               'separateWordSearch': true,
               'debug': false,
               'filter': function(node, term, totalCounter, counter){
                        if($.inArray(term, stopwords) != -1){
                            return false;
                        }else{
                            return true;
                        }
                }
           };

    $(element).mark(term, options);
}

