---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

title: Helvault - FAQ
description: Answers to frequently asked questions about Helvault
layout: default
---
<html>
  <head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="style.css">
  </head>
  
  <script type="text/javascript">
    function openContentIfNeeded() {
      if (window.location.hash !== "") {
        const collapseElementList = document.querySelectorAll(window.location.hash)
        const collapseList = [...collapseElementList].map(collapseEl => new bootstrap.Collapse(collapseEl))
      }
    }
    window.onload = openContentIfNeeded;
  </script>
</html>

# Helvault FAQ
Below you'll find answers to common questions you may have about Helvault. If you need extra support consider [reaching us out]({{site.helvault_support_form}}) or [joining our Discord server](https://discord.gg/vD78aV58VZ).

{% assign titles = "" | split: "" %}
{% assign hrefs = "" | split: "" %}
{% assign descriptions = "" | split: "" %}


{% assign titles = titles | push: "Why there's a new Helvault app instead of just updating the old one?" %}
{% assign hrefs = hrefs | push: "new" %}
{% assign descriptions = descriptions | push: "We appreciate the support and would like to clarify the reasons behind the need for creating a new Helvault.<br/>First of all, we understand how depreciative a subscription based model is to users, and that is why we do not have recurring subscriptions on the app. However, development of new features + maintenance takes time and money. We needed a way to keep new stuff coming in without forcing users to keep paying.<br/><br/>The solution was to implement an 'opt-in' style where you are free to continue using what you paid for, but in case the new stuff brings enough value you can decide to upgrade to the new app. This works by keeping the 'current' (now legacy) app working just as expected, but also bringing a new one so users who see enough value can move to.<br/><br/>In short, if the new app and its features bring value to you and you'd like to support the future of Helvault, welcome aboard! Otherwise you have all the means to keep using the legacy app for as long as you please." %}


{% assign titles = titles | push: "Will Helvault Legacy stop working?" %}
{% assign hrefs = hrefs | push: "legacy" %}
{% assign descriptions = descriptions | push: "No! The app will continue to work normally, receiving maintenance updates in case a new OS update introduces bugs. The only change is that it will no longer receive feature updates." %}


{% assign titles = titles | push: "What new features should I expect on the new app?" %}
{% assign hrefs = hrefs | push: "newFeatures" %}
{% assign descriptions = descriptions | push: "1. Added support for iCloud Sync, one of the most requested featured by the community<br/>2. Added iPad support<br/>3. Added Mac support<br/>4. Added new filtering and sorting options on the Collection section<br/>5. Improved pricing support with much faster reload<br/>6. Reworked the scanner so it supports offline scanning <i>(offline scanning is not yet available, will be coming soon on a future update)</i>" %}


{% assign titles = titles | push: "Why my purchases from the Legacy app are not restored on the new app?" %}
{% assign hrefs = hrefs | push: "restore" %}
{% assign descriptions = descriptions | push: "As mentioned above, the Legacy app will continue to work normally, as is, so your purchases are and will always be yours. With that being said, by AppStore rules purchases cannot be carried over between apps. In case the new app has value to you, items will need to be purchased separately." %}


{% assign titles = titles | push: "How can I migrate my content from the Legacy app to the new one?" %}
{% assign hrefs = hrefs | push: "migrate" %}
{% assign descriptions = descriptions | push: "You can migrate your content (cards, binders and lists) from the Legacy app to the new one by doing the following:<br/>1. Open the new Helvault app<br/>2. On the 'Collections' area, go to Settings (three-dotted button on the top left corner)<br/>3. Scroll down and tap 'Import from Helvault Legacy'<br/><br/>That's it! Now you just need to follow on-screen instructions." %}


{% assign titles = titles | push: "Some cards from newly released sets are missing... Why?" %}
{% assign hrefs = hrefs | push: "newCards" %}
{% assign descriptions = descriptions | push: "Helvault uses Scryfall as a provider for cards. Usually newly released sets are added pretty quickly (specially on the English language), but sometimes delays may happen.<br/><br/>You could also <a href='https://scryfall.com/contact'>reach Scryfall directly</a> to get a sense of when your cards will be added." %}


{% assign titles = titles | push: "Why can't I add some cards in languages other than English?" %}
{% assign hrefs = hrefs | push: "missingCards" %}
{% assign descriptions = descriptions | push: "Helvault uses Scryfall as a provider for cards. Usually they prioritize adding cards first on the English language, meaning it may take some time until other languages such as Italian, Spanish, Japanese etc appear on Helvault.<br/>As a workaround you could keep the card in English on your collection and add a <code>tag</code> to it with the language name. This way you can still keep track of the cards that are represented by the English version instead of their printed version.<br/><br/>You could also <a href='https://scryfall.com/contact'>reach Scryfall directly</a> to get a sense of when your cards will be added." %}


{% assign titles = titles | push: "How are card prices calculated?" %}
{% assign hrefs = hrefs | push: "prices" %}
{% assign descriptions = descriptions | push: "Helvault uses Scryfall as a provider for cards and their prices. You can check the exact parameters for price calculation on <a href='https://scryfall.com/docs/faqs/where-do-scryfall-prices-come-from-7' target='_blank'>this page</a>." %}


{% assign titles = titles | push: "Some of my cards have missing prices. What can I do?" %}
{% assign hrefs = hrefs | push: "missingPrices" %}
{% assign descriptions = descriptions | push: "Card prices are calculated using the current market as a base (you can check more details <a href='https://scryfall.com/docs/faqs/where-do-scryfall-prices-come-from-7' target='_blank'>here</a>). If one or more cards on your collection have their price missing, and you have already attempted to reload them on the 'Stats' section, it means that currently the market does not have enough listings to have an estimated price." %}


{% assign titles = titles | push: "I'm trying to import my cards via CSV but the app is not recognizing them... Why?" %}
{% assign hrefs = hrefs | push: "import" %}
{% assign descriptions = descriptions | push: "The main way of importing cards via CSV is using the Helvault format, which contains the following columns: <code>extras</code>, <code>name</code>, <code>scryfall_id</code>, <code>quantity</code>.<br/>You can also use other PRO formats such as Plain List, TCG Player, Deckbox and many others after purchasing the 'PRO Import and Export' feature." %}


{% assign titles = titles | push: "I'm trying to export my cards via CSV into another app/website but they don't recognize it... What can I do?" %}
{% assign hrefs = hrefs | push: "export" %}
{% assign descriptions = descriptions | push: "There is no unified CSV format for card import/export, so each app prefer its own... Here are some suggestions on what you can do to import cards in other services:<br/><br/>1. Edit the headers of the CSV file on your computer... Maybe they expect <code>card_name</code> instead of <code>name</code>.<br/>2. Reach them out asking for expected CSV formats if you don't already know.<br/>3. If you need more columns on your CSV file such as <code>price</code>, <code>set code</code>, <code>set name</code>, <code>oracle id</code> etc, take a look at the 'Helvault PRO CSV' format. It's a single-purchase (not a subscription) that may help you." %}


{% assign titles = titles | push: "How does iCloud Sync work?" %}
{% assign hrefs = hrefs | push: "icloud" %}
{% assign descriptions = descriptions | push: "When you enable iCloud Sync by purchasing the 'iCloud Sync' feature you will leverage the power of iCloud to have all your content (such as cards, binders, lists, prices etc) synchronized between your devices.<br/>Keep in mind that the larger the change the longer it takes for sync to complete. For instance, if you add a new card on device 'A' you should be seeing that card on device 'B' pretty much instantly. However if you import 1000 cards via CSV it might take a while for them to appear on all devices.<br/><br/>You can check the iCloud Sync status of your device by doing the following:<br/><br/>1. Open the Helvault app<br/>2. On the 'Collections' area, go to Settings (three-dotted button on the top left corner)<br/>3. Scroll down and tap 'iCloud Syncing'" %}


{% assign titles = titles | push: "iCloud Sync is taking too long... What's going on?" %}
{% assign hrefs = hrefs | push: "icloudThrottle" %}
{% assign descriptions = descriptions | push: "When you import a large amount of data at once (such as a long CSV file, or backup from the Legacy app) iCloud will automatically throttle the rate of the data transfer to preserver their servers stability. Unfortunately this is not something Helvault can control, all apps (including Apple's own) are affected by this process. Moreover, completion time does not appear to be linear so the more you sync at once the longer it will take.<br/><br/>Here are some estimations you might use as guide:<br/><br/>- 500 cards should finish uploading almost instantly<br/>- 3,000 cards should finish uploading in about 5 minutes<br/>- 14,000 cards should finish uploading in about 4.5 hours<br/><br/>Keep in mind that these numbers may vary considerably depending on a number of factors such as iCloud servers availability, your internet connection speed, your physical distance to iCloud servers and more." %}


{% assign titles = titles | push: "iCloud Sync isn't working. What can I do?" %}
{% assign hrefs = hrefs | push: "icloudFix" %}
{% assign descriptions = descriptions | push: "If you have purchased the 'iCloud Sync' feature and suspect that content is not syncing properly between devices, here are some things you can do:<br/><br/>1. Verify that you are signed-in with iCloud on your device. More details <a href='https://support.apple.com/en-gb/guide/icloud/mmfc0f1e2a/1.0/icloud/1.0' target='_blank'>here</a>.<br/>2. Within the app, go to <code>Settings → iCloud Syncing</code> and check that <code>iCloud Account</code> is displayed as <code>Available</code> and <code>Setup</code> displays as <code>Successful</code>. If any of these are displayed otherwise, check step <code>1</code> above.<br/>3. Make sure that Helvault has permissions to use iCloud. You can do so by going to <code>Settings → [your name] → iCloud → Show All (under the APPS USING ICLOUD section)</code>. On this page the toggle should be turned ON for Helvault. If you cannot reach this page, check step <code>1</code> above." %}

<div class="faq-body">
  {% for i in (1..titles.size) %}
  {% assign index = i | minus: 1 %}
    <div class="faq-collapse-item">
      <a class="faq-collapse-btn" data-bs-toggle="collapse" href="#{{ hrefs[index] }}">{{ titles[index] }}</a>
      <div class="faq-collapse-content collapse" id="{{ hrefs[index] }}"><br/>{{ descriptions[index] }}</div>
    </div>
  {% endfor %}
</div>