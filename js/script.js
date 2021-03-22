//function showApps () {
//    var name = document.getElementById("name").value;
//    var industry = document.getElementById("industry").value;
//    var bad_message = "Hey Dumbass " + name + "!" + " I can't believe you come from the " + industry + " industry! Hahahaha";
//    var good_message = "Hi " + name + "!" + " Wow! You come from the " + industry + " industry! I am very impressed!";
//
//
//    if (industry.length < 6) {
//        document.querySelector("#content").textcontent = good_message;
//    }
//
//    else {avas
//        document.querySelector("#content").textcontent = bad_message;
//    }
//
//}
//
//
//document.addEventListener("DOMContentLoaded",function() {
//    document.querySelector(".navbar-toggler").addEventListener("blur", function (event) {
//        var screenWidth = window.innerWidth;
//        if (screenWidth < 768) {
//            document.querySelector(".navbar-toggler").collapse('hide');
//        }
//    });
//});

"use strict";

const $navbarNav = $("#navbarNav");
if ($navbarNav) {
  const navbarNavCollapse = (event) => {
    if (
      !$navbarNav.is(event.target) &&
      $navbarNav.has(event.target).length === 0
    ) {
      $navbarNav.collapse("hide");
      document.removeEventListener("mouseup", navbarNavCollapse);
    }
  };

  $navbarNav.on("shown.bs.collapse", () => {
    document.addEventListener("mouseup", navbarNavCollapse);
  });
}

function showApps() {
  var name = document.getElementById("name").value;
  var industry = document.getElementById("industry").value;
  var bad_message =
    "Hey Dumbass " +
    name +
    "!" +
    " I can't believe you come from the " +
    industry +
    " industry! Hahahaha";
  var good_message =
    "Hi " +
    name +
    "!" +
    " Wow! You come from the " +
    industry +
    " industry! I am very impressed!";

  if (industry.length < 6) {
    document.querySelector("#content").textContent = good_message;
  } else {
    document.querySelector("#content").textContent = bad_message;
  }
}

const modal = document.querySelector(".modal");
const overlay = document.querySelector(".overlay");
const btnCloseModal = document.querySelector(".close-modal");
const btnsOpenModal = document.querySelectorAll(".show-modal");

const openModal = function () {
  modal.classList.remove("hidden");
  overlay.classList.remove("hidden");
};

const closeModal = function () {
  modal.classList.add("hidden");
  overlay.classList.add("hidden");
};

for (let i = 0; i < btnsOpenModal.length; i++)
  btnsOpenModal[i].addEventListener("click", openModal);

btnCloseModal.addEventListener("click", closeModal);
overlay.addEventListener("click", closeModal);

document.addEventListener("keydown", function (e) {
  // console.log(e.key);

  if (e.key === "Escape" && !modal.classList.contains("hidden")) {
    closeModal();
  }
});

//function sayHello () {
//    var name =
//     document.getElementById("name").value;
//     var message = "<h2>Hello " + name + "!</h2>";
//
//    // document
//    //   .getElementById("content")
//    //   .textContent = message;
//
//    document.getElementById("content").innerHTML = message;
//
//    if (name === "student") {
//      var title =
//        document
//          .querySelector("#title")
//          .textContent;
//      title += " & Lovin' it!";
//      document
//          .querySelector("h1")
//          .textContent = title;
//    }
//  }
