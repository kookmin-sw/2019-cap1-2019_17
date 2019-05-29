! function (t) {
	t(document).ready(function () {
		t(".lang-selector").off("click").on("click", function () {
			location.href = location.pathname + "?lang=" + t(this).data("lang")
		})
	})
}(jQuery),
function (t) {
	"use strict";
	"function" == typeof define && define.amd ? define(["jquery"], t) : t(jQuery)
}(function (o) {
	"use strict";
	var n = [],
		e = [],
		s = {
			precision: 100,
			elapse: !1,
			defer: !1
		};
	e.push(/^[0-9]*$/.source), e.push(/([0-9]{1,2}\/){2}[0-9]{4}( [0-9]{1,2}(:[0-9]{2}){2})?/.source), e.push(/[0-9]{4}([\/\-][0-9]{1,2}){2}( [0-9]{1,2}(:[0-9]{2}){2})?/.source), e = new RegExp(e.join("|"));
	var p = {
			Y: "years",
			m: "months",
			n: "daysToMonth",
			d: "daysToWeek",
			w: "weeks",
			W: "weeksToMonth",
			H: "hours",
			M: "minutes",
			S: "seconds",
			D: "totalDays",
			I: "totalHours",
			N: "totalMinutes",
			T: "totalSeconds"
		},
		a = function (t, e, i) {
			this.el = t, this.$el = o(t), this.interval = null, this.offset = {}, this.options = o.extend({}, s), this.firstTick = !0, this.instanceNumber = n.length, n.push(this), this.$el.data("countdown-instance", this.instanceNumber), i && ("function" == typeof i ? (this.$el.on("update.countdown", i), this.$el.on("stoped.countdown", i), this.$el.on("finish.countdown", i)) : this.options = o.extend({}, s, i)), this.setFinalDate(e), !1 === this.options.defer && this.start()
		};
	o.extend(a.prototype, {
		start: function () {
			null !== this.interval && clearInterval(this.interval);
			var t = this;
			this.update(), this.interval = setInterval(function () {
				t.update.call(t)
			}, this.options.precision)
		},
		stop: function () {
			clearInterval(this.interval), this.interval = null, this.dispatchEvent("stoped")
		},
		toggle: function () {
			this.interval ? this.stop() : this.start()
		},
		pause: function () {
			this.stop()
		},
		resume: function () {
			this.start()
		},
		remove: function () {
			this.stop.call(this), n[this.instanceNumber] = null, delete this.$el.data().countdownInstance
		},
		setFinalDate: function (t) {
			this.finalDate = function (t) {
				if (t instanceof Date) return t;
				if (String(t).match(e)) return String(t).match(/^[0-9]*$/) && (t = Number(t)), String(t).match(/\-/) && (t = String(t).replace(/\-/g, "/")), new Date(t);
				throw new Error("Couldn't cast `" + t + "` to a date object.")
			}(t)
		},
		update: function () {
			if (0 !== this.$el.closest("html").length) {
				var t, e = new Date;
				t = this.finalDate.getTime() - e.getTime(), t = Math.ceil(t / 1e3), t = !this.options.elapse && t < 0 ? 0 : Math.abs(t), this.totalSecsLeft === t || this.firstTick ? this.firstTick = !1 : (this.totalSecsLeft = t, this.elapsed = e >= this.finalDate, this.offset = {
					seconds: this.totalSecsLeft % 60,
					minutes: Math.floor(this.totalSecsLeft / 60) % 60,
					hours: Math.floor(this.totalSecsLeft / 60 / 60) % 24,
					days: Math.floor(this.totalSecsLeft / 60 / 60 / 24) % 7,
					daysToWeek: Math.floor(this.totalSecsLeft / 60 / 60 / 24) % 7,
					daysToMonth: Math.floor(this.totalSecsLeft / 60 / 60 / 24 % 30.4368),
					weeks: Math.floor(this.totalSecsLeft / 60 / 60 / 24 / 7),
					weeksToMonth: Math.floor(this.totalSecsLeft / 60 / 60 / 24 / 7) % 4,
					months: Math.floor(this.totalSecsLeft / 60 / 60 / 24 / 30.4368),
					years: Math.abs(this.finalDate.getFullYear() - e.getFullYear()),
					totalDays: Math.floor(this.totalSecsLeft / 60 / 60 / 24),
					totalHours: Math.floor(this.totalSecsLeft / 60 / 60),
					totalMinutes: Math.floor(this.totalSecsLeft / 60),
					totalSeconds: this.totalSecsLeft
				}, this.options.elapse || 0 !== this.totalSecsLeft ? this.dispatchEvent("update") : (this.stop(), this.dispatchEvent("finish")))
			} else this.remove()
		},
		dispatchEvent: function (t) {
			var m, e = o.Event(t + ".countdown");
			e.finalDate = this.finalDate, e.elapsed = this.elapsed, e.offset = o.extend({}, this.offset), e.strftime = (m = this.offset, function (t) {
				var e, i, s, o, n, a = t.match(/%(-|!)?[A-Z]{1}(:[^;]+;)?/gi);
				if (a)
					for (var l = 0, r = a.length; l < r; ++l) {
						var d = a[l].match(/%(-|!)?([a-zA-Z]{1})(:[^;]+;)?/),
							c = (e = d[0].toString().replace(/([.?*+^$[\]\\(){}|-])/g, "\\$1"), new RegExp(e)),
							h = d[1] || "",
							u = d[3] || "",
							f = null;
						d = d[2], p.hasOwnProperty(d) && (f = p[d], f = Number(m[f])), null !== f && ("!" === h && (s = f, n = o = void 0, o = "s", n = "", (i = u) && (1 === (i = i.replace(/(:|;|\s)/gi, "").split(/\,/)).length ? o = i[0] : (n = i[0], o = i[1])), f = 1 < Math.abs(s) ? o : n), "" === h && f < 10 && (f = "0" + f.toString()), t = t.replace(c, f.toString()))
					}
				return t.replace(/%%/, "%")
			}), this.$el.trigger(e)
		}
	}), o.fn.countdown = function () {
		var s = Array.prototype.slice.call(arguments, 0);
		return this.each(function () {
			var t = o(this).data("countdown-instance");
			if (void 0 !== t) {
				var e = n[t],
					i = s[0];
				a.prototype.hasOwnProperty(i) ? e[i].apply(e, s.slice(1)) : null === String(i).match(/^[$A-Z_][0-9A-Z_$]*$/i) ? (e.setFinalDate.call(e, i), e.start()) : o.error("Method %s does not exist on jQuery.countdown".replace(/\%s/gi, i))
			} else new a(this, s[0], s[1])
		})
	}
}),
function (t) {
	t(document).ready(function () {
		t(".pop-close").click(function () {
			t(this).parents("div#contents").hide()
		})
	})
}(jQuery), $(function () {
	var t = $(window).width();
	num = 0, setInterval(function () {
		++num;
		var t = $(".visual-img li").length - 1;
		$(".visual-img li.curr").removeClass("curr"), $(".visual-img li").eq(num).addClass("curr"), num == t && (num = -1)
	}, 4e3);
	var e = $(".logo-area ul"),
		i = e.find("li").outerWidth(!0),
		s = e.find("li").length,
		o = i * s;

	function n() {
		var t = $(window).width();
		$(".team li").removeClass(), 768 < t && t < 1440 ? $("[data-tablet-right]").addClass("right") : $("[data-align-right]").addClass("right")
	}
	e.css("width", o), setInterval(function () {
		e.css("width", o), e.stop().animate({
			left: -i + "px"
		}, function () {
			$(this).css("left", 0), $(".logo-area li:first-child").appendTo(".logo-area ul")
		})
	}, 2e3), $(".content-slide .slider").bxSlider({
		mode: "horizontal",
		speed: 500,
		pager: !0,
		moveSlides: 1,
		slideWidth: 1240,
		minSlides: 1,
		maxSlides: 1,
		slideMargin: 0,
		auto: !1,
		autoHover: !1,
		controls: !0
	}), $(".media-slider .slider").bxSlider({
		mode: "horizontal",
		speed: 500,
		pager: !0,
		moveSlides: 1,
		slideWidth: 1240,
		minSlides: 1,
		maxSlides: 1,
		slideMargin: 0,
		auto: !1,
		autoHover: !1,
		controls: !0
	}), $(".t_media-slider .slider").bxSlider({
		mode: "horizontal",
		speed: 500,
		pager: !0,
		moveSlides: 1,
		slideWidth: 616,
		minSlides: 1,
		maxSlides: 1,
		slideMargin: 0,
		auto: !1,
		autoHover: !1,
		controls: !0
	}), $(".m_media-slider .slider").bxSlider({
		mode: "horizontal",
		speed: 500,
		pager: !1,
		moveSlides: 1,
		slideWidth: 280,
		minSlides: 1,
		maxSlides: 1,
		slideMargin: 0,
		auto: !1,
		autoHover: !1,
		controls: !0
	}), $(".video-slider .slider").bxSlider({
		mode: "horizontal",
		speed: 500,
		pager: !0,
		moveSlides: 1,
		slideWidth: 1240,
		minSlides: 1,
		maxSlides: 1,
		slideMargin: 0,
		auto: !1,
		autoHover: !1,
		controls: !0
	}), $(".m_video-slider .slider").bxSlider({
		mode: "horizontal",
		speed: 500,
		pager: !0,
		moveSlides: 1,
		minSlides: 1,
		maxSlides: 1,
		slideMargin: 0,
		auto: !1,
		autoHover: !1,
		controls: !0
	}), $(".btn-youtube").on("click", function () {
		var t = $(this).attr("data-youtube"),
			e = ""; - 1 < t.indexOf("?v=") ? e = t.split("?v=")[1] : -1 < t.indexOf("youtu.be") && (e = t.split("https://youtu.be/")[1]);
		var i = '<iframe id="vod-player" class="vod-player" allowfullscreen title="Video player" src="' + ("https://www.youtube.com/embed/" + e + "?showinfo=0&amp;wmode=transparent&amp;autoplay=1&amp;rel=0") + '" marginwidth="0" marginheight="0" frameborder="0" scrolling="no"></iframe>';
		return $(".youtube_wrap .youtube_box").html("").append(i), $(".youtube_wrap").addClass("view"), !1
	}), $(".youtube_wrap .close").on("click", function () {
		return $(".youtube_box").html(""), $(".youtube_wrap").removeClass("view"), !1
	}), $(window).on("resize", function () {
		t <= 1024 && $(".content-slide .slider").bxSlider({
			mode: "horizontal",
			speed: 500,
			pager: !0,
			moveSlides: 1,
			slideWidth: 280,
			minSlides: 1,
			maxSlides: 1,
			slideMargin: 0,
			auto: !1,
			autoHover: !1,
			controls: !0
		}), n()
	}), n(), $(".select-box button").on("click mouseover", function () {
		$(this).next().css("display", "block"), $(this).addClass("on")
	}), $(".select-box").on("mouseleave", function () {
		$(".select-box div").css("display", "none"), $(this).parent().find("button").removeClass("on")
	}), $(".select-box li a").on("click", function () {
		$(".select-box div").css("display", "none");
		var t = $(this).html();
		$(this).parents(".select-box").find("button").html(t)
	}), $(".top").on("click", function () {
		$("html, body").animate({
			scrollTop: 0
		}, 800, function () {})
	}), $(".more").on("click", function () {
		var t = $(".team ul").height();
		$(".more-box").animate({
			height: t
		}), $(this).css("opacity", 0), $(window).on("resize", function () {
			$(".more-box").css("height", "auto")
		})
	}), $(".select_box button").on("click", function () {
		$(this).hasClass("on") ? ($(this).next().slideUp(), $(this).removeClass("on"), $(this).parent().removeClass("open"), $(".route_wrap > .dim").fadeOut()) : ($(this).next().slideDown(), $(this).addClass("on"), $(this).parent().addClass("open"), $(".route_wrap > .dim").fadeIn()), $(".select_box").hasClass("open") && $("body").removeClass("overScroll")
	}), $(".select_box li a").on("click", function () {
		var t = $(this).html();
		$(".select_box .select_list").slideUp(), $(".route_wrap > .dim").fadeOut(), $(this).parents(".select_box").find("button").html(t), $(this).parent().addClass("active").siblings().removeClass("active"), $(".select_box button").removeClass("on"), $(".select_box").removeClass("open")
	}), $(".btn-menu").on("click", function () {
		$("#contents").addClass("dim"), $(".mobile-nav").animate({
			left: 0
		}, 500)
	}), $(".mobile-nav .close, .mobile-nav a").on("click", function () {
		$("#contents").removeClass("dim"), $(".mobile-nav").animate({
			left: "-248px"
		}, 500)
	}), $(".faq-list li a").on("click", function () {
		$(this).parent().hasClass("on") ? $(this).parent().removeClass("on") : ($(".faq-list li.on").removeClass("on"), $(this).parent().addClass("on"))
	})
});