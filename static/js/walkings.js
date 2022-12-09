// 현재 시간 받아 오기 & 오늘 이후 날짜로 설정 new Date().toISOString()
document.getElementById('walk_date').value = new Date().toISOString().slice(0, -8);
document.getElementById('walk_date').min = new Date().toISOString().slice(0, -8);

//-------------------------------디테일 맵 설정-------------------------------------------------------
function detailMap(e) {

  const latitude = document.querySelector(`#park_lat-${e}`).innerText
  const longtitude = document.querySelector(`#park_lon-${e}`).innerText
  const parkName = document.querySelector(`#parkname-${e}`).innerText
  //------------------------------------지도 기본 설정--------------------------------------------
  var mapContainer = document.getElementById(`detail-map-${e}`), // 지도를 표시할 div
    mapOption = {
      center: new kakao.maps.LatLng(latitude, longtitude), // 지도의 중심좌표
      level: 5 // 지도의 확대 레벨
    };


  // 지도를 생성합니다    
  var map = new kakao.maps.Map(mapContainer, mapOption);

  // 지도를 현재 위치 중심으로 이동
  var currentPos = new kakao.maps.LatLng(latitude, longtitude)
  map.setCenter(currentPos)
  map.panTo(currentPos);

  // 마커 이미지의 이미지 크기 입니다
  var imageSrc = "/static/images/dog2.png";
  var imageSize = new kakao.maps.Size(30, 30);

  var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

  // 마커를 생성합니다
  var marker = new kakao.maps.Marker({
    map: map,
    position: new kakao.maps.LatLng(latitude, longtitude), // 마커를 표시할 위치
    //  title: , // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
    image: markerImage, // 마커 이미지
    clickable: true,
  });

  setTimeout(function () { map.relayout(); map.setCenter(currentPos); }, 500);

  var iwContent = `<div class="detailmap-info">${parkName}</div>`, // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
    iwPosition = new kakao.maps.LatLng(latitude, longtitude), //인포윈도우 표시 위치입니다
    iwRemoveable = false; // removeable 속성을 ture 로 설정하면 인포윈도우를 닫을 수 있는 x버튼이 표시됩니다

  // 인포윈도우를 생성하고 지도에 표시합니다
  var infowindow = new kakao.maps.InfoWindow({
    position: iwPosition,
    content: iwContent,
    removable: iwRemoveable
  });

  infowindow.open(map, marker);

}

//-----------------------------------------메인 지도------------------------------------------------------
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
const options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0
};



// 마커 이미지의 이미지 크기 입니다
var imageSrc = "/static/images/dog2.png";
var imageSize = new kakao.maps.Size(30, 30);

function mapSearch(latitude, longitude) {

  var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
      center: new kakao.maps.LatLng(latitude, longitude), // 지도의 중심좌표
      level: 6 // 지도의 확대 레벨
    };

  // 지도를 생성합니다    
  var map = new kakao.maps.Map(mapContainer, mapOption);

  // 지도를 현재 위치 중심으로 이동
  var currentPos = new kakao.maps.LatLng(latitude, longitude)
  map.panTo(currentPos);

  // 내 위치 마커 생성
  var marker = new kakao.maps.Marker({
    position: currentPos,
    image: new kakao.maps.MarkerImage("/static/images/5894087.png", new kakao.maps.Size(50, 50))
  })

  // 기존에 마커가 있다면 제거
  marker.setMap(null)
  marker.setMap(map)

  axios({ method: 'get', url: `/walkings/search/${latitude}/${longitude}` })
    .then(response => {

      var parksJson = response.data.parksJson


      for (let i = 0; i < parksJson.length; i++) {
        var data = parksJson[i]
        displayMarker(data)
      }

      function displayMarker(data) {
        // 마커 이미지를 생성합니다    
        var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);

        // 마커를 생성합니다
        var marker = new kakao.maps.Marker({
          map: map, // 마커를 표시할 지도
          position: new kakao.maps.LatLng(data.latitude, data.longitude), // 마커를 표시할 위치
          image: markerImage, // 마커 이미지
          clickable: true,
        });

        var overlay = new kakao.maps.CustomOverlay({
          yAnchor: 1.3,
          position: marker.getPosition(),
        })
        // 커스텀 오버레이에 표시할 컨텐츠 입니다

        var overlayContent = document.createElement('div')
        overlayContent.classList.add('wrap');

        var overlayInfo = document.createElement('div')
        overlayInfo.classList.add('info');

        var overlayTitle = document.createElement('div')
        overlayTitle.classList.add('title')
        overlayTitle.innerText = data.parkName

        var closeBtn = document.createElement('div')
        closeBtn.classList.add('close')
        closeBtn.onclick = function () {
          overlay.setMap(null)
        }


        var overlayBody = document.createElement('div')
        overlayBody.classList.add('body')

        var overlayBodyContent1 = document.createElement('p')
        overlayBodyContent1.classList.add('overlay-text')
        overlayBodyContent1.innerHTML = '<i class="bi bi-map"></i> ' + data.address

        var overlayBodyContent2 = document.createElement('p')
        overlayBodyContent2.classList.add('overlay-text')
        overlayBodyContent2.innerHTML = '<i class="bi bi-geo-alt-fill"></i> 나와의 거리 ' + data.distance

        var choiceBtn = document.createElement('button')
        choiceBtn.classList.add('btn')
        choiceBtn.innerHTML = ' <i class="bi bi-pin-map-fill"></i> 같이 산책하기'
        choiceBtn.setAttribute('data-parkname', `${data.parkName}`)
        choiceBtn.setAttribute('data-park-id', `${data.park_pk}`)
        choiceBtn.setAttribute('onclick', 'pick_park(this)')

        overlayTitle.append(closeBtn)
        overlayBody.append(overlayBodyContent1, overlayBodyContent2, choiceBtn)
        overlayInfo.append(overlayTitle, overlayBody)
        overlayContent.append(overlayInfo)

        overlay.setContent(overlayContent)

        kakao.maps.event.addListener(marker, 'click', function () {
          overlay.setMap(map)
        })

        // select-option에 추가할 내용
        var option = document.createElement('option')
        option.innerText = data.parkName + `  (약 ${data.distance})`;
        option.classList.add('parkSelect-options')
        option.value = data.park_pk
        parkSelect.append(option)

      }// 마커 반복문 종료

    })

}

function success(pos) {
  const latitude = pos.coords.latitude
  const longitude = pos.coords.longitude

  console.log(latitude)
  console.log(longitude)
  console.log("성공")
  mapSearch(latitude, longitude)

}


function error(err) {
  console.log("실패")
  console.warn(`ERROR(${err.code}): ${err.message}`);
}

function pick_park(e) {
  const parkSelectOptions = document.querySelectorAll('.parkSelect-options')

  for (let i = 0; i < parkSelectOptions.length; i++) {
    if (parkSelectOptions[i].value === event.target.dataset.parkId) {
      parkSelectOptions[i].setAttribute('selected', true)
      break;
    }
  }

  // // 아래는 비동기 코드
  // const walking_form = document.querySelector('#walking_form')
  // walking_form.setAttribute('park-id', `${event.target.dataset.parkId} `)
  // const walk_form_btn = document.querySelector('#walk_form_btn')
  // walk_form_btn.setAttribute('data-park-id', `${event.target.dataset.parkId} `)
}

// function w_create(e) {
//   console.log("산책 약속 잡기 실행")
//   const walking_form = document.querySelector('#walking_form')
//   event.preventDefault();
//   axios({
//     method: 'post',
//     url: `/walkings/create/${event.target.dataset.parkId}`,
//     headers: { 'X-CSRFToken': csrftoken },
//     data: new FormData(walking_form)
//   })
//     .then(response => {
//       console.log(response.data)
//       const dogroup_data = (response.data.dogroup_data)
//       console.log(dogroup_data)
//     })
// }


// 인원수 카운트 하는 코드
const walkCnt = document.querySelector('#walk_cnt')

function counter(type) {
  let number = walkCnt.value;

  if (type === 'minus') {
    number = parseInt(number) - 1
  } else if (type === 'plus') {
    number = parseInt(number) + 1
  }
  // walkCnt.value = number 도 가능하나, element의 변화가 없음
  walkCnt.setAttribute('value', number)

  counterCheck(number)
}

function counterCheck(number) {
  if (number < 1 || number > 6) {
    alert('지정가능한 범위를 벗어났습니다.')
    walkCnt.setAttribute('value', 3)
    walkCnt.value = 3
  } else if (number == 1) {
    alert('같이 산책하기 위한 최소 인원은 2명입니다.')
    counter('plus')
  } else if (number == 6) {
    alert('같이 산책하기 위한 최대 인원은 5명까지 입니다.')
    counter('minus')
  }
}

walkCnt.addEventListener('change', function (event) {
  let number = walkCnt.value;

  counterCheck(number)
})

locationSearchForm = document.querySelector('#location-search-form')
locationSearchForm.addEventListener('submit', function (event) {
  event.preventDefault();
  const address = document.querySelector('#address').value


  // 주소-좌표 변환 객체를 생성합니다
  var geocoder = new kakao.maps.services.Geocoder();

  // 주소로 좌표를 검색합니다
  geocoder.addressSearch(address, function (result, status) {

    // 정상적으로 검색이 완료됐으면 
    if (status === kakao.maps.services.Status.OK) {

      var coords = new kakao.maps.LatLng(result[0].y, result[0].x);

      mapSearch(result[0].y, result[0].x)
    }
  });
});


navigator.geolocation.getCurrentPosition(success, error, options);
