import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

telephoneNumber = os.getenv('TELEPHONE_NUMBER')
bearer_token = os.getenv('BEARER_TOKEN')

# 네이버 API 엔드포인트
url = "https://api.commerce.naver.com/external/v2/products"

# HTML 콘텐츠
html_content = """
<div class="aplus-v2 desktop celwidget" cel_widget_id="aplus" data-csa-c-id="at25eo-21ss7i-fl20j7-vjyt27" data-cel-widget="aplus">
        <style type="text/css">

.aplus-v2 .premium-aplus-module-2 .premium-background-wrapper {
    position: relative;
}

.aplus-v2 .premium-aplus-module-2 .premium-intro-wrapper {
    position: absolute;
    width: 50%;
    height: 100%;
    top: 0;
}

.aplus-v2 .premium-aplus-module-2 .premium-intro-wrapper.right {
    left: 50%;
}

html[dir="rtl"] .aplus-v2 .premium-aplus-module-2 .premium-intro-wrapper.right {
    left: auto;
    right: 50%;
}

.aplus-v2 .premium-aplus-module-2 .premium-intro-wrapper.secondary-color {
    color: #fff;
}

.aplus-v2 .premium-aplus-module-2 .premium-intro-background {
    padding: 20px;
}

.aplus-v2 .premium-aplus-module-2 .aplus-module-2-topic {
    padding-bottom: 10px;
}

.aplus-v2 .premium-aplus-module-2 .aplus-module-2-heading {
    padding-bottom: 20px;
}

.aplus-v2 .premium-aplus-module-2 .aplus-module-2-description {
    line-height: 1.5em;
}

.aplus-v2 .premium-aplus-module-2 .premium-intro-background.white-background {
    background: rgba(255,255,255,0.5);
}

.aplus-v2 .premium-aplus-module-2 .premium-intro-background.black-background {
    background: rgba(0,0,0,0.5);
}

.aplus-v2 .premium-aplus-module-2 .premium-intro-background.black-background,
.aplus-v2 .premium-aplus-module-2 .premium-intro-background.black-background h1,
.aplus-v2 .premium-aplus-module-2 .premium-intro-background.black-background h5,
.aplus-v2 .premium-aplus-module-2 .premium-intro-background.black-background ol,
.aplus-v2 .premium-aplus-module-2 .premium-intro-background.black-background ul,
.aplus-v2 .premium-aplus-module-2 .premium-intro-background.black-background ol .a-list-item,
.aplus-v2 .premium-aplus-module-2 .premium-intro-background.black-background ul .a-list-item {
  color: #fff;
}

.aplus-v2 .premium-aplus-module-2 .premium-intro-content-container {
    display: table;
    height: 100%;
}

.aplus-v2 .premium-aplus-module-2 .premium-intro-wrapper.left .premium-intro-content-container {
    padding-left: 40px;
}

html[dir="rtl"] .aplus-v2 .premium-aplus-module-2 .premium-intro-wrapper.left .premium-intro-content-container {
	padding-left: 0px;
	padding-right: 40px;
}

.aplus-v2 .premium-aplus-module-2 .premium-intro-wrapper.right .premium-intro-content-container {
    padding-right: 40px;
}

html[dir="rtl"] .aplus-v2 .premium-aplus-module-2 .premium-intro-wrapper.right .premium-intro-content-container {
    padding-right: 0px;
    padding-left: 40px;
}

.aplus-v2 .premium-aplus-module-2 .premium-intro-content-column {
    display: table-cell;
    vertical-align: middle;
}


</style>
       <script type="text/javascript">(function(f) {var _np=(window.P._namespace("PremiumAplusModule"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {
P.now('premium-module-5-comparison-table-scroller').execute(function(init){
    if (init) {
        return;
    }
    P.register('premium-module-5-comparison-table-scroller', function(){
        return function() {
            P.when('jQuery', 'a-popover', 'A', 'ready').execute(function($, popover, A) {
                function initCompTable(module) {
                    /**
                    * Premium comparison table: popover trigger module
                    */
                    var comparisonName = $(module).data('comparison-name');
                    (function() {
                        var $additionalInfo = $('.aplus-v2 .aplus-popover-trigger');
                        $additionalInfo.each(function(i, trigger) {
                            return popover.create(trigger, $(trigger).data());
                        });
                        $additionalInfo.hover(
                            function() {
                                $(this).focus();
                            }
                        );
                    })();
                    /**
                    * Premium comparison table: adjust column width module
                    */
                    (function() {
                        var VISIBLE_COLUMNS = 4.2;  /* How many visible columns on load */
                        var MIN_WIDTH = 230;
                        var getWidth = function() {
                            return $(this).outerWidth();
                        }
                        /* cache selectors */
                        var
                            $container = $('.aplus-v2 .comparison-table #'+comparisonName),
                            $header = $('.aplus-v2 .comparison-table #'+comparisonName+' td.attribute'),
                            $slider = $('.aplus-v2 .comparison-table #'+comparisonName+' .table-slider'),
                            $columns = $('.aplus-v2 .comparison-table #'+comparisonName+' .aplus-data-column'),
                            $activeColumn = $('.aplus-v2 .comparison-table #'+comparisonName+' .aplus-data-column.active.active-item');

                        /* Formula for determining desired column width */

                        var calculatedColumnWidth = Math.floor(
                            ($container.innerWidth() - $header.innerWidth()) / VISIBLE_COLUMNS
                        );

                        var childWidths = $activeColumn.map(getWidth).get();
                        var maxChildWidth = Math.max(MIN_WIDTH, Math.max.apply(Math, childWidths));
                        var minColumnWidth = $columns.innerWidth();
                        var calculatedPadding = $header.innerWidth() + maxChildWidth;

                        /* set the min-width of each column to the calulated width or minWidth */
                        $columns.css(
                            'min-width',
                            Math.max(MIN_WIDTH, (calculatedColumnWidth < minColumnWidth
                                ? calculatedColumnWidth
                                : minColumnWidth))
                        );
                        $activeColumn.css('width', maxChildWidth);

                        /* AUI RTL script automatically changes this to padding-right under RTL context */
                        $slider.css('padding-left', calculatedPadding);

                        /* show the component */
                        $container.removeClass('loading');
                    })();
                    /**
                    * Premium comparison table: top scroll bar
                    */
                    (function() {
                        /* cache selectors */
                        var
                            $header = $('.aplus-v2 .comparison-table #'+comparisonName+' td.attribute'),
                            $fixedColumn = $('.aplus-v2 .comparison-table #'+comparisonName+' td.active'),
                            $scrollWrapperTop = $('.aplus-v2 .comparison-table #'+comparisonName+' .scroll-wrapper-top'),
                            $scrollWrapperBottom = $('.aplus-v2 .comparison-table #'+comparisonName+' .scroll-wrapper-bottom'),
                            $scrollWidth = $('.aplus-v2 .comparison-table #'+comparisonName+' .scroll-width'),
                            $scrollBar = $('.aplus-v2 .comparison-table #'+comparisonName+' .scroll-bar');
                        /* confirm fixed column exists and can add width to the total width of the scroll bar */
                        var fixedColumnWidth = $fixedColumn.innerWidth();
                        if ( fixedColumnWidth === null ) {
                            fixedColumnWidth = 0;
                        }
                        /* set width of scrollBar */
                        $scrollBar.css('width', $scrollWidth.innerWidth() + fixedColumnWidth + $header.innerWidth());
                        /* connect scrolls together */
                        $scrollWrapperTop.scroll(function() {
                            $scrollWrapperBottom.scrollLeft($scrollWrapperTop.scrollLeft());
                        });
                        $scrollWrapperBottom.scroll(function() {
                            $scrollWrapperTop.scrollLeft($scrollWrapperBottom.scrollLeft());
                        });
                    })();
                }

                $('.aplus-v2 .premium-aplus-module-5 .table-container').each(function(index, module) {
                    initCompTable(module);
                });
            });
        }
    });
});
}));</script>       <style type="text/css">

/**
 * Premium-module 5: Comparision table - scroller
 */

.aplus-v2 .premium-aplus-module-5 h1 {
    padding-bottom: 30px;
}

/* position column-headers relative to this table */
.aplus-v2 .premium-aplus-module-5 .table-container {
    position: relative;
    opacity: 1;
}

.aplus-v2 .premium-aplus-module-5 .table-container.loading {
    opacity: 0;
}

.aplus-v2 .premium-aplus-module-5 .table-slider {
    overflow-x: scroll;
    overflow-y: visible;
    width: 100%;
}

/* left column headers are absolute positioned */
.aplus-v2 .premium-aplus-module-5 td.attribute {
    position: absolute;
    width: 300px;
    top: auto;
    left: 0;
}

html[dir="rtl"] .aplus-v2 .premium-aplus-module-5 td.attribute {
    right: 0px;
    left: auto;
}

.aplus-v2 .premium-aplus-module-5 td.active-item {
    position: absolute;
    top: auto;
    left: 300px;
}

html[dir="rtl"]  .premium-aplus-module-5 td.active-item {
    left: auto;
    right: 300px;
}

.aplus-v2 .premium-aplus-module-5 .attribute,
.aplus-v2 .premium-aplus-module-5 .active-item,
.aplus-v2 .premium-aplus-module-5 .description {
    font-size: 16px;
    font-family: arial;
    line-height: 2.5em;
    white-space:nowrap;
    color: #000;
}

.aplus-v2 .premium-aplus-module-5 .attribute,
.aplus-v2 .premium-aplus-module-5 .active-item,
.aplus-v2 .premium-aplus-module-5 .description {
    font-family: inherit;
}

.aplus-v2 .premium-aplus-module-5 table.a-bordered td.attribute,
.aplus-v2 .premium-aplus-module-5 table.a-bordered td.active-item {
    background-color: #fff;
    z-index: 100;
}

.aplus-v2 .premium-aplus-module-5 table.a-bordered tr:nth-child(even) td.attribute,
.aplus-v2 .premium-aplus-module-5 table.a-bordered tr:nth-child(even) td.active-item {
    background-color: #f0f2f2;
}

.aplus-v2 .premium-aplus-module-5 table.a-bordered tr:nth-child(even):last-child td.attribute {
    border-bottom: #f0f2f2 solid 1px;
}

/* Override AUI - the odd rows have a white background while the even ones have gray background */
.aplus-v2 .premium-aplus-module-5 table.a-bordered tr:nth-child(odd) {
    background-color: #fff;
}

.aplus-v2 .premium-aplus-module-5 table.a-bordered tr:nth-child(even) {
    background-color: #f0f2f2;
}

.aplus-v2 .premium-aplus-module-5 table.a-bordered td.attribute .comparison-metric-name {
    outline-style: none;
}

.aplus-v2 .premium-aplus-module-5 table.a-bordered td.attribute .aplus-popover-trigger::after {
    content: "?";
    display: inline-block;
    font-size: 12px;
    position: relative;
    bottom: 5px;
}

.aplus-v2 .premium-aplus-module-5 td.attribute.empty {
    height: 332px;
}

.aplus-v2 .premium-aplus-module-5 .header-img {
    padding-top: 10px;
}

/* Prevent table borders from overlapping */
.aplus-v2 .premium-aplus-module-5 table {
    border-collapse: separate;
}

/* Override default AUI .a-bordered table borders */
.aplus-v2 .premium-aplus-module-5 table.a-bordered td,
.aplus-v2 .premium-aplus-module-5 table.a-bordered th,
.aplus-v2 .premium-aplus-module-5 table.a-bordered {
    border-width: 0;
    border-color: #eaeaea;
    border-style: solid;
}

.aplus-v2 .premium-aplus-module-5 table.a-bordered td {
    border-right-width: 1px;
}

.aplus-v2 .premium-aplus-module-5 table.a-bordered td:last-child {
    border-right-width: 0;
}

html[dir="rtl"] .aplus-v2 .premium-aplus-module-5 table.a-bordered td:last-child {
    border-right-width: 1px;
}

/* Active column should be surrounded in darker border. */
.aplus-v2 .premium-aplus-module-5 table.a-bordered td.active {
    border-color: #767676;
    border-right-width: 1px;
    border-left-width: 1px;
}

/* Top Active column needs border-top */
.aplus-v2 .premium-aplus-module-5 table.a-bordered tr:first-child td.active {
    border-top-width: 1px;
    height: 332px;
}

/* Bottom column column needs border-bottom */
.aplus-v2 .premium-aplus-module-5 table.a-bordered tr:last-child td.active {
    border-bottom-width: 1px;
}

/* Size the top scroller */
.aplus-v2 .premium-aplus-module-5 .scroll-wrapper-top {
    width: 100%;
    height: 20px;
    overflow-x: scroll;
    overflow-y: visible;
}

.aplus-v2 .premium-aplus-module-5 .scroll-bar {
    height: 1px;
}

.aplus-v2 .premium-aplus-module-5 .add-to-cart {
    line-height: 1rem;
    font-weight: normal;
}

.aplus-v2 .premium-aplus-module-5 .review {
    font-size: 14px;
}
</style>
      <style type="text/css">

/**
 * Premium modules global styles
 */
.aplus-v2.desktop {
  max-width: 1464px;
  min-width: 800px;
  margin-left: auto;
  margin-right: auto;
  word-wrap: break-word;
  overflow-wrap: break-word;
  word-break: break-word;
}
/* Undo this for tech-specs because it breaks table layout */
.aplus-v2.desktop .premium-aplus .aplus-tech-spec-table { word-break: initial; }

.aplus-v2 .premium-aplus,
.aplus-v2 .premium-aplus .aplus-h1,
.aplus-v2 .premium-aplus .aplus-h2,
.aplus-v2 .premium-aplus .aplus-p1,
.aplus-v2 .premium-aplus .aplus-p2,
.aplus-v2 .premium-aplus .aplus-p3,
.aplus-v2 .premium-aplus .aplus-accent1,
.aplus-v2 .premium-aplus .aplus-accent2
{ font-family: Arial, sans-serif; }

.aplus-v2 .premium-aplus,
.aplus-v2 .premium-aplus .aplus-h1,
.aplus-v2 .premium-aplus .aplus-h2,
.aplus-v2 .premium-aplus .aplus-p1,
.aplus-v2 .premium-aplus .aplus-p2,
.aplus-v2 .premium-aplus .aplus-p3,
.aplus-v2 .premium-aplus .aplus-accent1,
.aplus-v2 .premium-aplus .aplus-accent2
{ font-family: inherit; }

/* type */
.aplus-v2 .premium-aplus .aplus-h1 { font-size: 32px; line-height: 1.2em; font-weight: 500; }
.aplus-v2 .premium-aplus .aplus-h2 { font-size: 26px; line-height: 1.25em; font-weight: 500; }
.aplus-v2 .premium-aplus .aplus-h3 { font-size: 18px; line-height: 1.25em; font-weight: 500; }
.aplus-v2 .premium-aplus .aplus-p1 { font-size: 20px; line-height: 1.3em; font-weight: 300; }
.aplus-v2 .premium-aplus .aplus-p2 { font-size: 16px; line-height: 1.4em; font-weight: 300; }
.aplus-v2 .premium-aplus .aplus-p3 { font-size: 14px; line-height: 1.4em; font-weight: 300; }
.aplus-v2 .premium-aplus .aplus-accent1 { font-size: 16px; line-height: 1.4em; font-weight: 600; }
.aplus-v2 .premium-aplus .aplus-accent2 { font-size: 14px; line-height: 1.4em; font-weight: 600; }

/* spacing */
.aplus-v2 .aplus-container-1 { padding: 40px; }
.aplus-v2 .aplus-container-1-2 { padding: 40px 80px; }
.aplus-v2 .aplus-container-2 { padding: 80px; }
.aplus-v2 .aplus-container-3 { padding: 40px 0; }

/* Display */
.aplus-v2 .premium-aplus .aplus-display-table { display: table; }
.aplus-v2 .premium-aplus .aplus-display-table-cell { display: table-cell; }
.aplus-v2 .premium-aplus .aplus-display-inline-block { display: inline-block; }

/* Aplus display table with min-width 1000px and fill remaining space inside parent */
.aplus-v2.desktop .premium-aplus .aplus-display-table-width { min-width: 1000px; width: 100% }

/**
* Padding and margin for element should be 10, 20, 40, or 80 px. Considering mini 10, small 20, medium 40, large 80.
*/

</style>
      <style type="text/css">

.premium-aplus-module-15 {
    padding: 40px 0;
    text-align: left;
}

.aplus-v2 .premium-aplus-module-15 {
    text-align: inherit;
}

.aplus-v2 .premium-aplus-module-15 .premium-aplus-15-heading-text {
    padding-bottom: 20px;
}

.aplus-v2 .premium-aplus-module-15 p {
    padding-bottom: 10px;
}

</style>
      <style type="text/css">

/**
 * Premium-module 12: Nav Carousel
 */

.aplus-v2 .premium-aplus-module-12 .aplus-carousel-card {
    position: relative;
    width: 100%;
}

.aplus-v2 .premium-aplus-module-12 .aplus-carousel-container {
    position: relative;
}

.aplus-v2 .premium-aplus-module-12 .aplus-image-carousel-container {
    /* Match the aspect ratio of the desktop image uploaded via the editor (1464px x 600px) */
    padding-top: calc(600 / 1464 * 100%); /* ~40.983% */
    height: 0;
}

.aplus-v2 .premium-aplus-module-12 .aplus-image-carousel-container > div {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
}

/* Override AUI styles. It poorly attempts to measure the slide heights before waiting until images load. */
.aplus-v2 .premium-aplus-module-12 .a-carousel-viewport {
    height: 100% !important;
}

.aplus-v2 .premium-aplus-module-12 .aplus-card-image img {
    width: 100%;
    height: auto;
}

.aplus-v2 .premium-aplus-module-12 .aplus-card-details-wrapper {
    position: absolute;
    top: 0;
    width: 50%;
    height: 100%;
}

.aplus-v2 .premium-aplus-module-12 .aplus-card-detail {
    display: table;
    width: 100%;
    height: 100%
}

.aplus-v2 .premium-aplus-module-12 .card-description {
    text-align: left;
}

html[dir="rtl"] .aplus-v2 .premium-aplus-module-12 .card-description {
    text-align: right;
}

.aplus-v2 .premium-aplus-module-12 .aplus-table-cell {
    display: table-cell;
    vertical-align: middle;
}

.aplus-v2 .premium-aplus-module-12 .aplus-text-background {
    padding: 20px;
}

.aplus-v2 .premium-aplus-module-12 .aplus-text-background-color {
    background: rgba(0, 0, 0, 0.5);
}

.aplus-v2 .premium-aplus-module-12 .aplus-text-background-color,
.aplus-v2 .premium-aplus-module-12 .aplus-text-background-color h1,
.aplus-v2 .premium-aplus-module-12 .aplus-text-background-color h5,
.aplus-v2 .premium-aplus-module-12 .aplus-text-background-color ol,
.aplus-v2 .premium-aplus-module-12 .aplus-text-background-color ul,
.aplus-v2 .premium-aplus-module-12 .aplus-text-background-color ol .a-list-item,
.aplus-v2 .premium-aplus-module-12 .aplus-text-background-color ul .a-list-item {
    color: #fff;
}

.aplus-v2 .premium-aplus-module-12 .description {
    padding-top: 20px;
}

/* nav */
.aplus-v2 .premium-aplus-module-12 .aplus-carousel-actions {
    position: absolute;
    top: 20px;
    width: 100%;
    text-align: center;
}

.aplus-v2 .premium-aplus-module-12 .aplus-goto-btn {
    display: inline-block;
    margin: 7px 10px;
    cursor: pointer;
    border-radius: 30px;
    border: 2px solid #000;
    line-height: 2.5em;
    min-width: 200px;
    background-color: #fff;
    white-space: nowrap;
    color: #000;
}

.aplus-v2 .premium-aplus-module-12 .aplus-carousel-index {
    display: none;
}

.aplus-v2 .premium-aplus-module-12 .aplus-goto-btn.aplus-active {
    border-color: #fff;
    background-color: #000;
    color: #fff;
}

/**
 * Regimen template specific css
 */

.aplus-v2 .premium-aplus-module-12 .aplus-goto-btn.regimen {
    text-align: left;
}

html[dir="rtl"] .aplus-v2 .premium-aplus-module-12 .aplus-goto-btn.regimen {
    text-align: right;
}

.aplus-v2 .premium-aplus-module-12 .aplus-carousel-actions.regimen {
    text-align: right;
    top: 50%;
    width: 250px;
    right: 75px;
    -webkit-transform: translateY(-50%);
    -moz-transform: translateY(-50%);
    -o-transform: translateY(-50%);
    transform: translateY(-50%);
}

html[dir="rtl"] .aplus-v2 .premium-aplus-module-12 .aplus-carousel-actions.regimen {
    text-align: left;
    top: 50%;
    left: 75px;
    right: auto;
}

.aplus-v2 .premium-aplus-module-12 .aplus-goto-btn.regimen {
    display: inline-block;
    margin: 10px 10px;
    cursor: pointer;
    border-radius: 30px;
    border: 2px solid #000;
    line-height: 2.5em;
    width: 220px;
    background-color: #fff;
    white-space: nowrap;
}

.aplus-v2 .premium-aplus-module-12 .aplus-goto-btn.regimen.aplus-active {
    border-color: #fff;
    background-color: #000;
    color: #fff;
}

.aplus-v2 .premium-aplus-module-12 .aplus-carousel-actions .regimen .aplus-carousel-index {
    display: inline-block;
    margin-left: 6px;
    width: 16px;
    line-height: 26px;
    color: #000;
    text-align: center;
}

html[dir="rtl"] .aplus-v2 .premium-aplus-module-12 .aplus-carousel-actions .regimen .aplus-carousel-index {
    margin-left: 0px;
    margin-right: 6px;
}

.aplus-v2 .premium-aplus-module-12 .aplus-goto-btn.regimen.aplus-active .aplus-carousel-index {
    color: #fff;
}

.aplus-v2 .premium-aplus-module-12 .aplus-headline-top.regimen {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #000;
    opacity: 0.5;
    text-align: center;
}

.aplus-v2 .premium-aplus-module-12 .aplus-headline-top.regimen .aplus-headline {
    color: #fff;
    line-height: 2em;
}

/**
 * Navigation template specific css
 */

.aplus-v2 .premium-aplus-module-12--top-nav .aplus-carousel-actions {
    background-color: rgba(0, 0, 0, 0.8);
    top: 0px;
}

.aplus-v2 .premium-aplus-module-12--top-nav .aplus-goto-btn {
    padding: 8px;
    color: #fff;
    background-color: transparent;
    border: none;
}

.aplus-v2 .premium-aplus-module-12--top-nav .aplus-goto-btn.aplus-active {
    text-decoration: underline;
    text-underline-offset: 0.8em;
    text-decoration-thickness: 3px;
    background-color: transparent;
    border: none;
}
</style>
       <script type="text/javascript">(function(f) {var _np=(window.P._namespace("PremiumAplusModule"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {
P.now('premium-module-12-nav-carousel').execute(function(init) {
    if (init) {
        return;
    }
    P.register('premium-module-12-nav-carousel', function(){
        return function() {
            P.when('A', 'jQuery', 'a-carousel-framework', 'ready').execute(function (A, $, framework) {
                function initiateCarousel(module) {
                    var MODULE_ID = $(module).data('module-id');
                    /**
                    * Carousel button element classname
                    * @const
                    */
                    var GOTO_BTN_CLASS_NAME = "aplus-goto-btn-" + MODULE_ID;
                    /**
                    * Carousel button element active classname
                    * @const
                    */
                    var GOTO_BTN_ACTIVE_CLASS_NAME = "aplus-active";
                    /**
                    * AUI name for aui carousel
                    * @const
                    */
                    var CAROUSEL_NAME = "premium-aplus-12-carousel-" + MODULE_ID;
                    /**
                    * Module class name
                    * @const
                    */
                    var MODULE_CLASS_NAME = ".aplus-v2 .premium-aplus-module-12";
                    /**
                    * Carousel text container class name
                    * @const
                    */
                    var TEXT_CONTAINER_CLASS_NAME = MODULE_CLASS_NAME + " .aplus-carousel-text-container-" + MODULE_ID;
                    /**
                    * Carousel text hidden class name
                    * @const
                    */
                    var TEXT_CONTAINER_HIDDEN = "aplus-hidden";
                    /**
                    * Carousel horizontal scroll container class name
                    * @const
                    */
                    var HORIZONTAL_SCROLL_CONTAINER_CLASS_NAME = MODULE_CLASS_NAME + " .aplus-horizontal-scroll-container-" + MODULE_ID;

                    function showCarouselText(oldIndex, newIndex) {
                        var oldClass = TEXT_CONTAINER_CLASS_NAME + "-" + oldIndex;
                        var newClass= TEXT_CONTAINER_CLASS_NAME + "-" + newIndex;
                        $(oldClass).addClass(TEXT_CONTAINER_HIDDEN);
                        $(newClass).removeClass(TEXT_CONTAINER_HIDDEN);
                    }

                    function scrollToCarouselButton(scrollLeft) {
                        if ($(HORIZONTAL_SCROLL_CONTAINER_CLASS_NAME).length) {
                            $(HORIZONTAL_SCROLL_CONTAINER_CLASS_NAME).animate({scrollLeft}, 200);
                        }
                    }

                    /**
                    * Creates a CarouselButton class for provided carousel instance
                    * @param {object} carousel - AUI Carousel instance
                    * @returns {Class} - CarouselButton Class
                    */
                    function CarouselButtonTemplate(carousel) {
                        /**
                        * Button for controlling the active slide
                        * @constructor
                        * @param {number} index - slide index
                        * @param {DOMElement} [elem] - optional DOM element to use as this objects DOM representation
                        */
                        function CarouselButton(index, elem) {
                            var self = this;
                            this.index = index;
                            this.carousel = carousel;

                            /* create the button element */
                            this.elem = this.getElem(elem);
                            this.$elem = $(this.elem);  /* store jquery version */
                            this.elem.addEventListener('click', self.handleClick.bind(self));

                            /* add this object to the object manager */
                            CarouselButton.objects.byId[index] = this;
                            CarouselButton.objects.all.push(this);
                        }

                        /**
                        * Describe behavior for click events on this.elem
                        * @memberOf CarouselButton
                        */
                        CarouselButton.prototype.handleClick = function(e) {
                            e.preventDefault();
                            this.carousel.gotoPage(this.index);
                        };

                        /**
                        * Enter active state
                        * @memberOf CarouselButton
                        */
                        CarouselButton.prototype.activate = function() {
                            this.$elem.addClass(GOTO_BTN_ACTIVE_CLASS_NAME);
                        };

                        /**
                        * Enter inactive state
                        * @memberOf CarouselButton
                        */
                        CarouselButton.prototype.deactivate = function() {
                            this.$elem.removeClass(GOTO_BTN_ACTIVE_CLASS_NAME);
                        };

                        /**
                        * Returns an existing or creates a new bound element for this object
                        * @memberOf CarouselButton
                        * @param {DOMElement} [elem] - optionally provide an existing element in the DOM to use
                        * @returns {DOMElement} - this objects DOM representation
                        */
                        CarouselButton.prototype.getElem = function(elem) {
                            if (this.elem) return this.elem;
                            if (elem) return elem;

                            var createdElem = document.createElement('span');
                            createdElem.className = GOTO_BTN_CLASS_NAME;

                            return createdElem;
                        };

                        /** @const Object manager */
                        CarouselButton.objects = {
                            byId: {},
                            all: [],
                        };

                        return CarouselButton;
                    }

                    framework.onInit(CAROUSEL_NAME, function(carousel) {
                        /** @const {Class} */
                        var CarouselButton = CarouselButtonTemplate(carousel);

                        /* create carousel controls */
                        var $carouselBtns = $(safeClassSelector(GOTO_BTN_CLASS_NAME));
                        var btns = $carouselBtns.map(function(i, btnElem) {
                            return new CarouselButton(i + 1, btnElem);
                        });

                        /* activate first one */
                        CarouselButton.objects.byId[1].activate();

                        /* Listen to slide changes */
                        A.on("a:carousel:" + CAROUSEL_NAME + ":change:pageNumber", function (data) {
                            var newCarouselButton = CarouselButton.objects.byId[data.newValue];
                            var marginLeft = parseInt(getComputedStyle(newCarouselButton.elem).getPropertyValue('margin-left'));
                            var positionLeft = newCarouselButton.elem.offsetLeft - marginLeft;

                            newCarouselButton.activate();
                            CarouselButton.objects.byId[data.oldValue].deactivate();
                            scrollToCarouselButton(positionLeft);
                            showCarouselText(data.oldValue, data.newValue);
                        });
                    });

                    /**
                    * @returns {string} - css classname prefixed with module selector
                    */
                    function safeClassSelector(className) {
                        return '.' + MODULE_CLASS_NAME + ' .' + className;
                    }
                }

                $('.aplus-v2 .premium-aplus-module-12 .aplus-carousel-container').each(function (index, module) {
                    initiateCarousel(module);
                });
                framework.createAll();
                framework.initializeAll();
            });
        }
    })
});
}));</script>                    <div class="celwidget aplus-module premium-module-2-fullbackground-image aplus-premium" cel_widget_id="aplus-premium-module-2-fullbackground-image" data-csa-c-id="1l6oo9-e7i5qm-3ztevk-k4ci6s" data-cel-widget="aplus-premium-module-2-fullbackground-image">
                            <div class="a-section a-spacing-none premium-aplus premium-aplus-module-2">                                  <div class="a-section a-spacing-none premium-background-wrapper">  <div class="a-section a-spacing-none background-image">                             <img alt="1" src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/dcbdd86c-c2da-40d7-abca-ec063cae0c4e.__CR0,0,2928,1200_PT0_SX1464_V1___.jpg" class="" data-src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/dcbdd86c-c2da-40d7-abca-ec063cae0c4e.__CR0,0,2928,1200_PT0_SX1464_V1___.jpg"><noscript><img alt="1" src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/dcbdd86c-c2da-40d7-abca-ec063cae0c4e.__CR0,0,2928,1200_PT0_SX1464_V1___.jpg"/></noscript>   </div>   </div> <div class="a-section a-text-center">                                  </div> </div>      </div>

         <div class="celwidget aplus-module premium-module-2-fullbackground-image aplus-premium" cel_widget_id="aplus-premium-module-2-fullbackground-image" data-csa-c-id="dzlfyw-wkgc80-jsgiyn-8qj0bg" data-cel-widget="aplus-premium-module-2-fullbackground-image">
                            <div class="a-section a-spacing-none premium-aplus premium-aplus-module-2">                                  <div class="a-section a-spacing-none premium-background-wrapper">  <div class="a-section a-spacing-none background-image">                             <img alt="3" src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/8c13883b-a979-442b-b262-1a8845fd76c3.__CR0,0,2928,1200_PT0_SX1464_V1___.jpg" class="" data-src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/8c13883b-a979-442b-b262-1a8845fd76c3.__CR0,0,2928,1200_PT0_SX1464_V1___.jpg"><noscript><img alt="3" src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/8c13883b-a979-442b-b262-1a8845fd76c3.__CR0,0,2928,1200_PT0_SX1464_V1___.jpg"/></noscript>   </div>   </div> <div class="a-section a-text-center">                                  </div> </div>      </div>

         <div class="celwidget aplus-module premium-module-2-fullbackground-image aplus-premium" cel_widget_id="aplus-premium-module-2-fullbackground-image" data-csa-c-id="1he98n-1hy0jk-jm27wu-o5bacr" data-cel-widget="aplus-premium-module-2-fullbackground-image">
                            <div class="a-section a-spacing-none premium-aplus premium-aplus-module-2">                                  <div class="a-section a-spacing-none premium-background-wrapper">  <div class="a-section a-spacing-none background-image">                             <img alt="3" src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/1b81c348-8f89-4810-8104-64781db1cdea.__CR0,0,1464,600_PT0_SX1464_V1___.jpg" class="" data-src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/1b81c348-8f89-4810-8104-64781db1cdea.__CR0,0,1464,600_PT0_SX1464_V1___.jpg"><noscript><img alt="3" src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/1b81c348-8f89-4810-8104-64781db1cdea.__CR0,0,1464,600_PT0_SX1464_V1___.jpg"/></noscript>   </div>   </div> <div class="a-section a-text-center">                                  </div> </div>      </div>

         <div class="celwidget aplus-module premium-module-12-nav-carousel aplus-premium" cel_widget_id="aplus-premium-module-12-nav-carousel" data-csa-c-id="e9ydz9-k7x529-9yn4mu-c3xxfn" data-cel-widget="aplus-premium-module-12-nav-carousel">
                                                              <div class="a-section a-spacing-none premium-aplus premium-aplus-module-12 premium-aplus-module-12--top-nav"> <div data-module-id="3" class="a-section a-spacing-none aplus-carousel-container"> <div id="premium-aplus-12-carousel-3-id" data-a-carousel-options="{&quot;peek_percentage&quot;:0,&quot;minimum_gutter_width&quot;:0,&quot;show_partial_next&quot;:false,&quot;name&quot;:&quot;premium-aplus-12-carousel-3&quot;}" data-a-display-strategy="single" data-a-transition-strategy="slideCircular" class="a-begin a-carousel-container a-carousel-display-single a-carousel-transition-slideCircular aplus-image-carousel-container a-carousel-initialized"><input autocomplete="on" type="hidden" class="a-carousel-firstvisibleitem">  <div class="a-row a-carousel-controls a-carousel-row a-carousel-has-buttons a-carousel-overlay-buttons a-carousel-rounded-buttons"><div class="a-carousel-row-inner"><div class="a-carousel-col a-carousel-left" style="visibility: visible;"><a class="a-carousel-goto-prevpage" tabindex="0" href="#"><i class="a-icon a-icon-previous-rounded"><span class="a-icon-alt">Previous page</span></i></a></div><div class="a-carousel-col a-carousel-center"><div class="a-carousel-viewport" id="anonCarousel5" style="height: 395px;"><ol class="a-carousel" role="list" style="width: 3856px; transition: all 0ms ease 0s; transform: translateX(-964px) translateZ(0px);"><li class="a-carousel-card aplus-carousel-card" role="listitem" aria-setsize="4" aria-posinset="4" aria-hidden="true" style="visibility: hidden; width: 964px; margin: 0px;"> <div class="a-section a-spacing-none aplus-card-image">                             <img alt="7" src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/19566465-680f-4cad-bbbb-49f906809417.__CR0,0,1464,600_PT0_SX1464_V1___.jpg">   </div>      </li><li class="a-carousel-card aplus-carousel-card" role="listitem" aria-setsize="4" aria-posinset="1" aria-hidden="false" style="visibility: visible; width: 964px; margin: 0px;"> <div class="a-section a-spacing-none aplus-card-image">                             <img alt="4" src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/06169aa6-6774-42a3-ba62-3f51f502d3eb.__CR0,0,1464,600_PT0_SX1464_V1___.jpg">   </div>      </li><li class="a-carousel-card aplus-carousel-card" role="listitem" aria-setsize="4" aria-posinset="2" aria-hidden="true" style="visibility: hidden; width: 964px; margin: 0px;"> <div class="a-section a-spacing-none aplus-card-image">                             <img alt="5" src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/27a48f8f-85ab-49e0-bfcb-ff48e3dfcb81.__CR0,0,1464,600_PT0_SX1464_V1___.jpg">   </div>      </li><li class="a-carousel-card aplus-carousel-card" role="listitem" aria-setsize="4" aria-posinset="3" aria-hidden="true" style="visibility: hidden; width: 964px; margin: 0px;"> <div class="a-section a-spacing-none aplus-card-image">                             <img alt="66" src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/26096e29-6987-4d17-91de-42a7b501e7ac.__CR0,0,1464,600_PT0_SX1464_V1___.jpg">   </div>      </li></ol></div></div><div class="a-carousel-col a-carousel-right" style="visibility: visible;"><a class="a-carousel-goto-nextpage" tabindex="0" href="#"><i class="a-icon a-icon-next-rounded"><span class="a-icon-alt">Next page</span></i></a></div></div></div> <span class="a-end aok-hidden"></span></div>  <div id="aplus-carousel-actions-3" class="a-section aplus-carousel-actions">     <span class="aplus-goto-btn aplus-goto-btn-3 aplus-active"> <span class="aplus-carousel-index">1</span> <span class="aplus-accent2 aplus-carousel-label">High-Speed Compatible</span> </span>      <span class="aplus-goto-btn aplus-goto-btn-3"> <span class="aplus-carousel-index">2</span> <span class="aplus-accent2 aplus-carousel-label">Superior Durability</span> </span>      <span class="aplus-goto-btn aplus-goto-btn-3"> <span class="aplus-carousel-index">3</span> <span class="aplus-accent2 aplus-carousel-label">Universal Compatibility</span> </span>      <span class="aplus-goto-btn aplus-goto-btn-3"> <span class="aplus-carousel-index">4</span> <span class="aplus-accent2 aplus-carousel-label">Hard-Wearing Exterior</span> </span>       </div> </div> </div>  <script type="text/javascript">(function(f) {var _np=(window.P._namespace("PremiumAplusModule"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {
    P.when('premium-module-12-nav-carousel').execute(function(init){
        init();
    });
}));</script>    </div>

         <div class="celwidget aplus-module premium-module-15-text aplus-premium" cel_widget_id="aplus-premium-module-15-text" data-csa-c-id="wnvqwr-7hz14l-thtfd7-8psh7n" data-cel-widget="aplus-premium-module-15-text">
                 <div class="a-section a-spacing-none premium-aplus premium-aplus-module-15"> <!-- Optional header -->
    <div class="a-section a-spacing-none premium-aplus-15-heading">                                   <h1 class="premium-aplus-15-heading-text a-text-bold"> New Nylon USB-C to USB-C Cable </h1>  </div> <div class="a-section a-spacing-none">                                   <p class="description"> Model Number: A8753<span class="a-text-bold">  </span>The Strong and Powerful Cable Bundle </p>     <p class="description"> <span class="a-text-bold">High-Speed Compatible: </span>Pair up with a 25W wall charger to charge a Samsung S20 to 55% in just 30 minutes. This device does not support 45W Samsung Super Fast Charging. </p>     <p class="description"> <span class="a-text-bold">Strong and Stylish: </span>The tough, yet stylish double-braided nylon exterior combines with a 12,000-bend lifespan for a cable that looks better and lasts longer than other brands. </p>     <p class="description"> <span class="a-text-bold">Transfer Files in Seconds: </span>Transfer movies, music, or an entire photo library in seconds with 480Mbps transfer speeds. </p>     <p class="description"> <span class="a-text-bold">Compatible Devices (Limited Charging Speeds): </span>MacBook Pro 16ʺ (2021), MacBook Pro 14ʺ (2021), MacBook Pro (2019/2018/2017/2016) 15.4ʺ, MacBook Pro 2020 16'', Lenovo ThinkPad X1 Series, HP Spectre Series. Samsung Galaxy S23+/S22+/S23 Ultra/S22 Ultra </p>     <p class="description"> <span class="a-text-bold">Fully Compatible Devices: </span>iPad Pro 2021/2020/2019/2018, iPad Air 4, iPad mini 6, Galaxy S23/S22/S21/S20/S10/S10+/S10e/S8/ S8+/ S9/ S9+/Galaxy Note 20 Ultra/20/10+/10/9/8, MacBook Pro (2020/2019/2018/2017/2016) 13.3ʺ, MacBook Air 2020/2019/2018, Google Pixel 3/4/5/6, Google Nexus 6P, Nintendo Switch, Huawei Matebook X </p>     <p class="description"> <span class="a-text-bold">Notes:</span> </p>     <p class="description"> This is a USB-C to USB-C cable, so it cannot be used with a USB-A charger. </p>     <p class="description"> This cable does not support media display. </p>    </div> </div>     </div>

         <div class="celwidget aplus-module premium-module-5-comparison-table-scroller aplus-premium" cel_widget_id="aplus-premium-module-5-comparison-table-scroller" data-csa-c-id="qzvahk-p1u9py-c88rm9-po0l07" data-cel-widget="aplus-premium-module-5-comparison-table-scroller">
                                                                                                     <div class="premium-aplus premium-aplus-module-5 aplus-container-3 comparison-table">
                                         <h1 class="a-text-center a-text-bold"> compared </h1>  <div id="comparison-table-container-5" data-comparison-name="comparison-table-container-5" class="a-section a-spacing-none table-container">  <div class="table-slider scroll-wrapper-bottom" style="padding-left: 529px;">
                <table class="a-bordered a-horizontal-stripes scroll-width">  <tbody><tr class="a-text-center">  <td class="attribute empty"></td>      <td class="aplus-data-column top-header active active-item a-text-bold" style="min-width: 230px; width: 230px;">     <a class="a-link-normal a-text-normal" title="60W USB C Cable" href="/dp/B088NRLMPV?ref=emc_p_m_5_i_atc">                             <img alt="1" src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/6ae4ee6a-adb9-42c1-98af-078e01489439.__CR0,0,200,225_PT0_SX200_V1___.jpg">   <p class="attribute a-text-bold"> 60W USB C Cable </p> </a>                 <form method="post" action="/cart/add-to-cart/ref=emc_p_m_5_i_atc"> <!-- sp:csrf --><input type="hidden" name="anti-csrftoken-a2z" value="hBPorEz7OXQgWGu2WhFa8bTqwfochrfaP1CE+BQWY056AAAAAGX4iHQ5M2M5YjZiMy1hMjg5LTQ2YjAtODI4ZS1kZjBhZTFhYTZjY2Y="><!-- sp:end-csrf -->
            <input type="hidden" name="items[0.base][asin]" value="B088NRLMPV"> <input type="hidden" name="items[0.base][offerListingId]" value="Y%2BIhKVrc%2B27Rled%2F0I7DbvqwV4V2%2Fzr8YSL5Gl9wIkUr37FVoA7pZSGlqrfxn9Y5UfZlODmB8MSPBbcsKlHVbVhIn795uAX9LjOao%2BNBywAHv6XRCzQM9IjQbHSpdcJHFNQzCHDeL1iwoBWepuJZidrgF1wWeE%2FVZmsdalYir68KKeIIVVlvcA%3D%3D"> <input type="hidden" name="items[0.base][quantity]" value="1"> <input type="hidden" name="clientName" value="Aplus_BuyableModules_DetailPage"> <div class="add-to-cart">
                <span id="add-to-cart-button" class="a-button a-spacing-small a-button-primary"><span class="a-button-inner"><input class="a-button-input" type="submit" aria-labelledby="add-to-cart-button-announce" control-id="ControlID-20"><span id="add-to-cart-button-announce" class="a-button-text" aria-hidden="true"> Add to Cart </span></span></span> </div>
        </form>            </td>      <td class="aplus-data-column top-header a-text-bold" style="min-width: 230px;">     <a class="a-link-normal a-text-normal" title="240W Right Angle Cable" href="/dp/B0CFZPSPBY?ref=emc_p_m_5_i_atc">                             <img alt="2" src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/7697a3ce-b6f0-4fde-938b-ccf39ac4adb5.__CR0,0,200,225_PT0_SX200_V1___.jpeg">   <p class="attribute a-text-bold"> 240W Right Angle Cable </p> </a>                 <form method="post" action="/cart/add-to-cart/ref=emc_p_m_5_i_atc"> <!-- sp:csrf --><input type="hidden" name="anti-csrftoken-a2z" value="hBPorEz7OXQgWGu2WhFa8bTqwfochrfaP1CE+BQWY056AAAAAGX4iHQ5M2M5YjZiMy1hMjg5LTQ2YjAtODI4ZS1kZjBhZTFhYTZjY2Y="><!-- sp:end-csrf -->
            <input type="hidden" name="items[0.base][asin]" value="B0CFZPSPBY"> <input type="hidden" name="items[0.base][offerListingId]" value="Y7OuoEtnJcz5TEiyBmdV4lioRra4vAhUiPjiNgN6OoK%2BVcrPpZs4GAuFGIUG9UA0HcsbNHlGYXZeZd2UCinc%2BWftrH5Spe8dQgdMja0A7zRaRczhxYw3x21RmE1HMuTfM6cc%2Forkv5qK8npE%2F7zzjHxN0uvwDEZ8u8LFIYytst6E5LTbZAkGKw%3D%3D"> <input type="hidden" name="items[0.base][quantity]" value="1"> <input type="hidden" name="clientName" value="Aplus_BuyableModules_DetailPage"> <div class="add-to-cart">
                <span id="add-to-cart-button" class="a-button a-spacing-small a-button-primary"><span class="a-button-inner"><input class="a-button-input" type="submit" aria-labelledby="add-to-cart-button-announce" control-id="ControlID-21"><span id="add-to-cart-button-announce" class="a-button-text" aria-hidden="true"> Add to Cart </span></span></span> </div>
        </form>            </td>      <td class="aplus-data-column top-header a-text-bold" style="min-width: 230px;">     <a class="a-link-normal a-text-normal" title="100W USB C Cable" href="/dp/B09LCJPZ1P?ref=emc_p_m_5_i_atc">                             <img alt="3" src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/c39bb73e-2d28-4fdb-8c23-f28045ffa8dc.__CR0,0,200,225_PT0_SX200_V1___.jpg">   <p class="attribute a-text-bold"> 100W USB C Cable </p> </a>                 <form method="post" action="/cart/add-to-cart/ref=emc_p_m_5_i_atc"> <!-- sp:csrf --><input type="hidden" name="anti-csrftoken-a2z" value="hBPorEz7OXQgWGu2WhFa8bTqwfochrfaP1CE+BQWY056AAAAAGX4iHQ5M2M5YjZiMy1hMjg5LTQ2YjAtODI4ZS1kZjBhZTFhYTZjY2Y="><!-- sp:end-csrf -->
            <input type="hidden" name="items[0.base][asin]" value="B09LCJPZ1P"> <input type="hidden" name="items[0.base][offerListingId]" value="EN6xgRrGHHh6KTtrS0bwGwT7%2FtRacMFRd%2BAHj4Tehc%2FDZAPiGNgOjh4TqmjIFZGVSY9VKxTqbk0zz325tzd7iPYKVedR7DphiwlHbMlkdCN%2FDMDxfbTJZZWQatoUb%2BNblUq36uBh5XaMTRZtCoABE5ORfvjm39bRv4Ub1kQ2njp1lJtIrkCGUg%3D%3D"> <input type="hidden" name="items[0.base][quantity]" value="1"> <input type="hidden" name="clientName" value="Aplus_BuyableModules_DetailPage"> <div class="add-to-cart">
                <span id="add-to-cart-button" class="a-button a-spacing-small a-button-primary"><span class="a-button-inner"><input class="a-button-input" type="submit" aria-labelledby="add-to-cart-button-announce" control-id="ControlID-22"><span id="add-to-cart-button-announce" class="a-button-text" aria-hidden="true"> Add to Cart </span></span></span> </div>
        </form>            </td>      <td class="aplus-data-column top-header a-text-bold" style="min-width: 230px;">     <a class="a-link-normal a-text-normal" title="100W Flow Cable" href="/dp/B093GGNRZM?ref=emc_p_m_5_i_atc">                             <img alt="4" src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/b012b7c0-b1b7-4f15-a2dd-90bee4cea721.__CR0,0,200,225_PT0_SX200_V1___.jpg">   <p class="attribute a-text-bold"> 100W Flow Cable </p> </a>                 <form method="post" action="/cart/add-to-cart/ref=emc_p_m_5_i_atc"> <!-- sp:csrf --><input type="hidden" name="anti-csrftoken-a2z" value="hBPorEz7OXQgWGu2WhFa8bTqwfochrfaP1CE+BQWY056AAAAAGX4iHQ5M2M5YjZiMy1hMjg5LTQ2YjAtODI4ZS1kZjBhZTFhYTZjY2Y="><!-- sp:end-csrf -->
            <input type="hidden" name="items[0.base][asin]" value="B093GGNRZM"> <input type="hidden" name="items[0.base][offerListingId]" value="QNfIGPQgMam814aFLAwR3mwsK%2BN9854axXEd6T3j3WPRpa2CY81KVL53FwWEP40l6UQKEbHJyVx3Bd3FIvw8TPMXxvW9p9NyQelvvHsp%2FUxcHZ2YAD3DlqEpwja%2FtWF9NEb9rR1fHi%2FeMZSImF70wBgMsdi3VyKTa1rwPBzWfzW8lFjldw6VyA%3D%3D"> <input type="hidden" name="items[0.base][quantity]" value="1"> <input type="hidden" name="clientName" value="Aplus_BuyableModules_DetailPage"> <div class="add-to-cart">
                <span id="add-to-cart-button" class="a-button a-spacing-small a-button-primary"><span class="a-button-inner"><input class="a-button-input" type="submit" aria-labelledby="add-to-cart-button-announce" control-id="ControlID-23"><span id="add-to-cart-button-announce" class="a-button-text" aria-hidden="true"> Add to Cart </span></span></span> </div>
        </form>            </td>      <td class="aplus-data-column top-header a-text-bold" style="min-width: 230px;">     <a class="a-link-normal a-text-normal" title="240W Bio-Braided Cable" href="/dp/B0C4FDJ8F7?ref=emc_p_m_5_i_atc">                             <img alt="5" src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/a4d6a2c2-9076-4a7c-8530-a228aef5f064.__CR0,0,200,225_PT0_SX200_V1___.jpg">   <p class="attribute a-text-bold"> 240W Bio-Braided Cable </p> </a>                 <form method="post" action="/cart/add-to-cart/ref=emc_p_m_5_i_atc"> <!-- sp:csrf --><input type="hidden" name="anti-csrftoken-a2z" value="hBPorEz7OXQgWGu2WhFa8bTqwfochrfaP1CE+BQWY056AAAAAGX4iHQ5M2M5YjZiMy1hMjg5LTQ2YjAtODI4ZS1kZjBhZTFhYTZjY2Y="><!-- sp:end-csrf -->
            <input type="hidden" name="items[0.base][asin]" value="B0C4FDJ8F7"> <input type="hidden" name="items[0.base][offerListingId]" value="TQKMEmsRN8%2FzdUiMInY0Ucb8eP5Rxgm609kl2QMbNxUzLUQrLChpHlESbeuh91Gq5NNYMeVrLd3DM5bOyjopZleQU8y6NaKzFmkYZ1vUlrrqgfpWcuxpZQO91TYVE64m8lQ0yfOn%2FtYWv5TE8vkmD1x8wrtTlBGmbIyM%2FWUMKS%2BRw2XS6ssb4w%3D%3D"> <input type="hidden" name="items[0.base][quantity]" value="1"> <input type="hidden" name="clientName" value="Aplus_BuyableModules_DetailPage"> <div class="add-to-cart">
                <span id="add-to-cart-button" class="a-button a-spacing-small a-button-primary"><span class="a-button-inner"><input class="a-button-input" type="submit" aria-labelledby="add-to-cart-button-announce" control-id="ControlID-24"><span id="add-to-cart-button-announce" class="a-button-text" aria-hidden="true"> Add to Cart </span></span></span> </div>
        </form>            </td>      <td class="aplus-data-column top-header a-text-bold" style="min-width: 230px;">     <a class="a-link-normal a-text-normal" title="USB A to USB C Cable" href="/dp/B0BPCZLFS4?ref=emc_p_m_5_i_atc">                             <img alt="6" src="https://m.media-amazon.com/images/S/aplus-media-library-service-media/69264fc9-12c1-4ccd-9567-d526076031f2.__CR0,0,200,225_PT0_SX200_V1___.jpg">   <p class="attribute a-text-bold"> USB A to USB C Cable </p> </a>                 <form method="post" action="/cart/add-to-cart/ref=emc_p_m_5_i_atc"> <!-- sp:csrf --><input type="hidden" name="anti-csrftoken-a2z" value="hBPorEz7OXQgWGu2WhFa8bTqwfochrfaP1CE+BQWY056AAAAAGX4iHQ5M2M5YjZiMy1hMjg5LTQ2YjAtODI4ZS1kZjBhZTFhYTZjY2Y="><!-- sp:end-csrf -->
            <input type="hidden" name="items[0.base][asin]" value="B0BPCZLFS4"> <input type="hidden" name="items[0.base][offerListingId]" value="V2NOoaxs8no%2B8C5zEUiDQRGaWRCxBUvtyaOW7uaZbUliBLaWssByC2uQpsELwtpyt5ldxyWrhhki2vdeaBsHk%2B39kVQxNidVLlFCeWgG%2FQa2eFLecBlABootO9MFuHM8zCAStDdKpEajwXYDvi0Ody%2BZNqkxHgxsQXbQULuqfZSEBHbp0AgtoQ%3D%3D"> <input type="hidden" name="items[0.base][quantity]" value="1"> <input type="hidden" name="clientName" value="Aplus_BuyableModules_DetailPage"> <div class="add-to-cart">
                <span id="add-to-cart-button" class="a-button a-spacing-small a-button-primary"><span class="a-button-inner"><input class="a-button-input" type="submit" aria-labelledby="add-to-cart-button-announce" control-id="ControlID-25"><span id="add-to-cart-button-announce" class="a-button-text" aria-hidden="true"> Add to Cart </span></span></span> </div>
        </form>            </td>      </tr>   <tr class="a-text-center">   <td class="a-text-left attribute a-text-bold"> <div tabindex="0" class="comparison-metric-name " data-inline-content="" data-position="triggerRight">
                                    <span class="a-text-bold"> Customer Reviews </span> </div>
                            </td>      <td class="aplus-data-column active active-item" style="min-width: 230px; width: 230px;">                    <div class="">
         <div class="a-size-base">
                    <i class="a-icon a-icon-star-small a-star-small-4-5 a-spacing-none"><span class="a-icon-alt">4.7 out of 5 stars</span></i> </div>
                <div class="a-size-small">41,101</div>
                </div> </td>      <td class="aplus-data-column" style="min-width: 230px;">                    <div class="">
         <div class="a-size-base">
                    <i class="a-icon a-icon-star-small a-star-small-4-5 a-spacing-none"><span class="a-icon-alt">4.6 out of 5 stars</span></i> </div>
                <div class="a-size-small">265</div>
                </div> </td>      <td class="aplus-data-column" style="min-width: 230px;">                    <div class="">
         <div class="a-size-base">
                    <i class="a-icon a-icon-star-small a-star-small-4-5 a-spacing-none"><span class="a-icon-alt">4.7 out of 5 stars</span></i> </div>
                <div class="a-size-small">11,874</div>
                </div> </td>      <td class="aplus-data-column" style="min-width: 230px;">                    <div class="">
         <div class="a-size-base">
                    <i class="a-icon a-icon-star-small a-star-small-5 a-spacing-none"><span class="a-icon-alt">4.8 out of 5 stars</span></i> </div>
                <div class="a-size-small">11,561</div>
                </div> </td>      <td class="aplus-data-column" style="min-width: 230px;">                    <div class="">
         <div class="a-size-base">
                    <i class="a-icon a-icon-star-small a-star-small-4-5 a-spacing-none"><span class="a-icon-alt">4.7 out of 5 stars</span></i> </div>
                <div class="a-size-small">3,197</div>
                </div> </td>      <td class="aplus-data-column" style="min-width: 230px;">                    <div class="">
         <div class="a-size-base">
                    <i class="a-icon a-icon-star-small a-star-small-4-5 a-spacing-none"><span class="a-icon-alt">4.7 out of 5 stars</span></i> </div>
                <div class="a-size-small">10,018</div>
                </div> </td>      </tr>   <tr class="a-text-center">   <td class="a-text-left attribute a-text-bold"> <div tabindex="0" class="comparison-metric-name " data-inline-content="" data-position="triggerRight">
                                    <span class="a-text-bold"> Price </span> </div>
                            </td>      <td class="aplus-data-column active active-item" style="min-width: 230px; width: 230px;">  <span class="description">
                                                       <span class="a-price" data-a-size="m" data-a-color="base"><span class="a-offscreen">$13.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">13<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span>     </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;">  <span class="description">
                                                       <span class="a-price" data-a-size="m" data-a-color="base"><span class="a-offscreen">$19.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">19<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span>     </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;">  <span class="description">
                                                       <span class="a-price" data-a-size="m" data-a-color="base"><span class="a-offscreen">$14.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">14<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span>     </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;">  <span class="description">
                                                       <span class="a-price" data-a-size="m" data-a-color="base"><span class="a-offscreen">$19.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">19<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span>     </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;">  <span class="description">
                                                       <span class="a-price" data-a-size="m" data-a-color="base"><span class="a-offscreen">$13.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">13<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span>     </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;">  <span class="description">
                                                       <span class="a-price" data-a-size="m" data-a-color="base"><span class="a-offscreen">$9.99</span><span aria-hidden="true"><span class="a-price-symbol">$</span><span class="a-price-whole">9<span class="a-price-decimal">.</span></span><span class="a-price-fraction">99</span></span></span>     </span>
                                    </td>      </tr>    <tr class="a-text-center">  <td class="a-text-left attribute a-text-bold"> <div tabindex="0" class="comparison-metric-name " data-inline-content="" data-position="triggerRight">
                                    <span class="a-text-bold"> Charging Technology </span> </div>
                            </td>      <td class="aplus-data-column active active-item" style="min-width: 230px; width: 230px;"> <span class="description">
                                                60W    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                240W    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                100W    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                100W    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                240W    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                15W    </span>
                                    </td>      </tr>  <tr class="a-text-center">  <td class="a-text-left attribute a-text-bold"> <div tabindex="0" class="comparison-metric-name " data-inline-content="" data-position="triggerRight">
                                    <span class="a-text-bold"> Length </span> </div>
                            </td>      <td class="aplus-data-column active active-item" style="min-width: 230px; width: 230px;"> <span class="description">
                                                1ft/3ft/6ft    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                6ft    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                3ft/6ft/10ft    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                3ft/6ft    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                3ft/6ft/10ft    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                3ft/6ft/10ft    </span>
                                    </td>      </tr>  <tr class="a-text-center">  <td class="a-text-left attribute a-text-bold"> <div tabindex="0" class="comparison-metric-name " data-inline-content="" data-position="triggerRight">
                                    <span class="a-text-bold"> Material </span> </div>
                            </td>      <td class="aplus-data-column active active-item" style="min-width: 230px; width: 230px;"> <span class="description">
                                                Braided    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                Braided    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                Braided    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                Silicone    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                Bio-Braided    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                Braided    </span>
                                    </td>      </tr>  <tr class="a-text-center">  <td class="a-text-left attribute a-text-bold"> <div tabindex="0" class="comparison-metric-name " data-inline-content="" data-position="triggerRight">
                                    <span class="a-text-bold"> Bend Lifespan </span> </div>
                            </td>      <td class="aplus-data-column active active-item" style="min-width: 230px; width: 230px;"> <span class="description">
                                                12000    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                10000    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                12000    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                25000    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                20000    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                10000    </span>
                                    </td>      </tr>  <tr class="a-text-center">  <td class="a-text-left attribute a-text-bold"> <div tabindex="0" class="comparison-metric-name " data-inline-content="" data-position="triggerRight">
                                    <span class="a-text-bold"> Data Transfer Speed </span> </div>
                            </td>      <td class="aplus-data-column active active-item" style="min-width: 230px; width: 230px;"> <span class="description">
                                                480Mbps    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                480Mbps    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                480Mbps    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                480Mbps    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                480Mbps    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                480Mbps    </span>
                                    </td>      </tr>  <tr class="a-text-center">  <td class="a-text-left attribute a-text-bold"> <div tabindex="0" class="comparison-metric-name " data-inline-content="" data-position="triggerRight">
                                    <span class="a-text-bold"> Media Display </span> </div>
                            </td>      <td class="aplus-data-column active active-item" style="min-width: 230px; width: 230px;"> <span class="description">
                                                X    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                X    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                X    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                X    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                X    </span>
                                    </td>      <td class="aplus-data-column" style="min-width: 230px;"> <span class="description">
                                                X    </span>
                                    </td>      </tr>  </tbody></table> </div>
        </div> </div>
 <script type="text/javascript">(function(f) {var _np=(window.P._namespace("PremiumAplusModule"));if(_np.guardFatal){_np.guardFatal(f)(_np);}else{f(_np);}}(function(P) {
    P.when('premium-module-5-comparison-table-scroller', 'ready').execute(function(init){ init() });
}));</script>     </div>

         </div>
"""


# 상품 등록을 위한 요청 본문
data = {
  "originProduct": {
    "statusType": "SALE",
    "saleType": "NEW",
    "leafCategoryId": "50003120",
    "name": "앵커 USB C to USB C 케이블",
    "detailContent": html_content,
    "images": {
      "representativeImage": {
         "url": "http://shop1.phinf.naver.net/20240319_287/1710792167833Ywjwb_JPEG/38700752818907409_2001105597.jpg"},
      # "optionalImages": ["추가 이미지 1 URL", "추가 이미지 2 URL"]
    },
    "salePrice": 21900,
    "stockQuantity": 100,
    "deliveryInfo": {
      "deliveryType": "DELIVERY",
      "deliveryAttributeType": "NORMAL",
      "deliveryCompany": "HANJIN",
      "deliveryFee": {
        "deliveryFeeType" : "FREE",
      },
      "claimDeliveryInfo": {
        "returnDeliveryFee": 50000,
        "exchangeDeliveryFee": 100000
      }
    },
    "detailAttribute": {
      "afterServiceInfo": {
        "afterServiceTelephoneNumber": telephoneNumber,
        "afterServiceGuideContent": "고객님의 부주의로 파손이 됐을 경우 A/S비용이 청구될 수도 있습니다."
      },
      "originAreaInfo": {
        "originAreaCode": "0204000",
        "importer": "앵커",
      },
      "minorPurchasable": True,
      "productInfoProvidedNotice": {
          "productInfoProvidedNoticeType": "OFFICE_APPLIANCES",
          "officeAppliances": {
              "returnCostREason": "",
              "noRefundReason": "",
              "qualityAssuranceStandard":"",
              "compensationProcedure": "",
              "troubleShootingContents": "",
              "itemName": "상품상세참조",
              "modelName": "상품상세참조",
              "certificationType": "상품상세참조",
              "releaseDateText": "상품상세참조",
              "manufacturer": "상품상세참조",
              "size": "상품상세참조",
              "specification": "상품상세참조",
              "warrantyPolicy": "상품상세참조",
              "afterServiceDirector": "상품상세참조",
          }
      },
      "sellerCodeInfo": {
          "sellerManagementCode": "https://www.amazon.com/"
          ,"sellerBarcode": "B088NRLMPV"
      },
      "certificationTargetExcludeContent": {
          "kcExemptionType": "OVERSEAS",
          "kcCertifiedProductExclusionYn": "KC_EXEMPTION_OBJECT"
      }
      
    },
  },
  "smartstoreChannelProduct": {
      "naverShoppingRegistration": True,
      "channelProductDisplayStatusType": "ON"
    }
}

# 요청 헤더
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + bearer_token
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# 응답 확인
if response.status_code == 200:
    # 성공적인 응답 처리
    print("성공:", response.json())
else:
    # 오류 응답 처리
    print("오류:", response.status_code, response.text)