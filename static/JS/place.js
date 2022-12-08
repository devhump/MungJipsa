function openCity(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("s21_tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";


  if ($(".s21_tab").position().top == 0) {//상단메뉴탭 탑이동 후 다른 탭 클릭시 컨텐츠 첫부분 보이게 수정 
    if (cityName == "info") {
      class_position = ".s21_de_food_img_st";
    } else if (cityName == "map_info") {
      class_position = ".s21_map_twrap";
    } else {
      class_position = ".s21_review_tit";
    }
    $('html').animate({ scrollTop: $(class_position).position().top + 40 }, 0);
  }

}
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();