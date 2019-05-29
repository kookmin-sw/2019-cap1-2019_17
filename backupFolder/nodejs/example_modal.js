if(typeof(Example) == "undefined") var Example = {};

(function($){
    Example.Modal = function() {
    this.initialize.apply(this,arguments);
}

Example.Modal.prototype = {
    initialize : function(hash) {
        var obj = this;

        // 멤버변수 정의
        this.hash = this.getHashData(hash);
        this.width = 0; // 콘텐츠 레이어 너비
        this.height = 0; // 콘텐츠 레이어 높이
        this.c_width = 0; // body 화면 너비
        this.c_height = 0; // body 화면 높이
        this.s_width = 0; // body 전체 너비
        this.s_height = 0; // body 전체 높이

        // 콘텐츠 레이어 사이즈 구하기(멤버변수에 저장)
        this.getLayerSize();

        // body 사이즈 구하기(멤버변수에 저장)
        this.getBodySize();

        // 추가 엘리먼트 생성
        this.addElement();

        // 마우스, 키 이벤트 정의
        this.addEvent();
    },

    // Hash 변수정의
    getHashData : function(hash) {
        if(typeof(hash.id) == "undefined") hash.id = "modal"; // 개체 아이디
        if(typeof(hash.is_slide) == "undefined") hash.is_slide = 0; // 슬라이딩 여부

        return hash;
    },

    // 추가 엘리먼트 생성 - JS에서 추가해 주어야 할 HTML 작성합니다.
    addElement : function() {
        // 배경 레이어 HTML 받아오기
        var html = this.addOverlay();

        // 배경레이어 HTML을 콘텐츠레이어 앞에 추가
        $("#"+this.hash.id).before(html);
    },

    // 마우스, 키 이벤트 정의
    addEvent : function() {
        var obj = this;

        // 닫기 버튼 클릭 이벤트 정의
        $("#"+this.hash.id+" .js_close").click(function() {
            // 모달창 감추기(여기서 obj는 Example.Modal 인스턴트 자체를 의미)
            obj.hide();
        });
    },

    /* 주요기능 */

    // 모달창 보여주기
    show : function() {
        // 가운데로 이동
        this.moveCenter();

        // 배경레이어 적용
        this.applyOverlay();

        // 콘텐츠 레이어 보여주기
        $("#"+this.hash.id).show();

        // 배경 레이어 보여주기
        $("#"+this.hash.id+"_overlay").show();
    },

    // 모달창 감추기
    hide : function() {
        $("#"+this.hash.id).hide(); // 콘텐츠 레이어 감추기
        $("#"+this.hash.id+"_overlay").hide(); // 배경 레이어 감추기
    },

    /* 부가 기능 */

    // 콘텐츠 레이어의 너비와 높이를 구해서 멤버변수에 정의
    getLayerSize : function() {
        this.width = $("#"+this.hash.id).outerWidth();
        this.height = $("#"+this.hash.id).outerHeight();
    },

    // body 사이즈 구해서 멤버변수에 정의
    getBodySize : function() {
        this.c_width = document.documentElement.clientWidth;
        this.c_height = document.documentElement.clientHeight;
        this.s_width = document.documentElement.scrollWidth;
        this.s_height = document.documentElement.scrollHeight;
    },

    // 배경 레이어 HTML 생성
    addOverlay : function() {
        var html = "";
        html += "<div id='"+this.hash.id+"_overlay' style='display:none;width:100%;position:absolute;top:0px;left:0px;opacity:0.5;background-color:#000000;z-Index:999'></div>";

        return html;
    },

    // 콘텐츠 레이어를 가운데로 이동(top, left 조절해 줌)
    moveCenter : function() {
        // left 좌표 구하기
        var left = Math.floor((this.c_width-this.width)/2);

        // top 좌표 구하기
        var res_height; // 콘텐츠를 화면상의 가운데로 두었을 때의 높이
        if(this.c_height < this.height) { // 화면 높이 < 콘텐츠 레이어 높이
            res_height = 0;
        } else { // 화면 높기 >= 콘텐츠 레이어 높이
            res_height = Math.floor((this.c_height-this.height)/2); // 차이를 빼서 2로 나눔. 그리고 내림.
        }
        var top = res_height+$(document).scrollTop(); // 화면상의 높이에 스크롤높이를 더한 절대좌표를 top에 저장

        // css의 top,left 조정
        $("#"+this.hash.id).css("top",top);
        $("#"+this.hash.id).css("left",left);
    },

    // 배경 레이어 적용
    applyOverlay : function() {
        // body 사이즈 구하기(멤버변수에 저장)
        this.getBodySize();

        // 배경 레이어에 width, height css 값 조정
        $("#"+this.hash.id+"_overlay").css("width",this.s_width);
        $("#"+this.hash.id+"_overlay").css("height",this.s_height);
    }
}

})
