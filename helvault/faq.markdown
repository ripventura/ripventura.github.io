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
Below you'll find answers to common questions about Helvault. If you need extra support, consider [reaching out to us]({{site.helvault_support_form}}) or [joining our Discord server](https://discord.gg/vD78aV58VZ).

{% assign titles = "" | split: "" %}
{% assign hrefs = "" | split: "" %}
{% assign descriptions = "" | split: "" %}


{% assign titles = titles | push: "Why is there a new Helvault app instead of just updating the old one?" %}
{% assign hrefs = hrefs | push: "new" %}
{% assign descriptions = descriptions | push: "We appreciate your support and would like to explain the reasons behind creating a new Helvault.<br/><br/>We understand how off-putting a subscription-based model can be for users, which is why we don't have recurring subscriptions in the app. However, developing new features and maintaining the app takes time and money. We needed a way to keep delivering new features without forcing users to keep paying.<br/><br/>The solution was to implement an 'opt-in' approach: you're free to continue using what you paid for, but if new features bring enough value, you can choose to upgrade to the new app. This works by keeping the 'current' (now Legacy) app working as expected, while also offering a new app for users who see enough value to switch.<br/><br/>In short, if the new app and its features bring value to you and you'd like to support the future of Helvault, welcome aboard! Otherwise, you have all the means to keep using the Legacy app for as long as you please." %}


{% assign titles = titles | push: "Will Helvault Legacy stop working?" %}
{% assign hrefs = hrefs | push: "legacy" %}
{% assign descriptions = descriptions | push: "No! The app will continue to work normally, receiving maintenance updates if a new OS update introduces bugs. The only change is that it will no longer receive feature updates." %}


{% assign titles = titles | push: "What new features should I expect in the new app?" %}
{% assign hrefs = hrefs | push: "newFeatures" %}
{% assign descriptions = descriptions | push: "1. Added support for iCloud Sync, one of the most requested features by the community<br/>2. Added iPad support<br/>3. Added Mac support<br/>4. Added new filtering and sorting options in the Collection section<br/>5. Improved pricing support with much faster reload<br/>6. Reworked the scanner to support offline scanning <i>(offline scanning is not yet available and will be coming in a future update)</i>" %}


{% assign titles = titles | push: "Why aren't my purchases from the Legacy app restored in the new app?" %}
{% assign hrefs = hrefs | push: "restore" %}
{% assign descriptions = descriptions | push: "As mentioned above, the Legacy app will continue to work normally, so your purchases are and will always be yours. However, App Store rules don't allow purchases to be transferred between apps. If the new app has value to you, items will need to be purchased separately." %}


{% assign titles = titles | push: "How can I migrate my content from the Legacy app to the new one?" %}
{% assign hrefs = hrefs | push: "migrate" %}
{% assign descriptions = descriptions | push: "You can migrate your content (cards, binders, and lists) from the Legacy app to the new one by following these steps:<br/>1. Open the new Helvault app<br/>2. In the 'Collections' area, go to Settings (three-dotted button in the top left corner)<br/>3. Scroll down and tap 'Import from Helvault Legacy'<br/><br/>That's it! Now just follow the on-screen instructions." %}


{% assign titles = titles | push: "Some cards from newly released sets are missing. Why?" %}
{% assign hrefs = hrefs | push: "newCards" %}
{% assign descriptions = descriptions | push: "Helvault uses Scryfall as its card data provider. Usually newly released sets are added quickly (especially for the English language), but sometimes delays may occur.<br/><br/>You can also <a href='https://scryfall.com/contact'>contact Scryfall directly</a> to get an estimate of when your cards will be added." %}


{% assign titles = titles | push: "Why can't I add some cards in languages other than English?" %}
{% assign hrefs = hrefs | push: "missingCards" %}
{% assign descriptions = descriptions | push: "Helvault uses Scryfall as its card data provider. They typically prioritize adding cards in English first, meaning it may take some time for other languages such as Italian, Spanish, or Japanese to appear in Helvault.<br/><br/>As a workaround, you could keep the card in English in your collection and add a <code>tag</code> with the language name. This way you can still track cards that are represented by the English version instead of their printed version.<br/><br/>You can also <a href='https://scryfall.com/contact'>contact Scryfall directly</a> to get an estimate of when your cards will be added." %}


{% assign titles = titles | push: "How are card prices calculated?" %}
{% assign hrefs = hrefs | push: "prices" %}
{% assign descriptions = descriptions | push: "Helvault uses Scryfall as its provider for cards and their prices. You can check the exact parameters for price calculation on <a href='https://scryfall.com/docs/faqs/where-do-scryfall-prices-come-from-7' target='_blank'>this page</a>." %}


{% assign titles = titles | push: "Some of my cards have missing prices. What can I do?" %}
{% assign hrefs = hrefs | push: "missingPrices" %}
{% assign descriptions = descriptions | push: "Card prices are calculated based on the current market (you can check more details <a href='https://scryfall.com/docs/faqs/where-do-scryfall-prices-come-from-7' target='_blank'>here</a>). If one or more cards in your collection have missing prices after you've tried to reload them in the 'Stats' section, it means the market currently doesn't have enough listings to determine an estimated price." %}


{% assign titles = titles | push: "I'm trying to import my cards via CSV but the app isn't recognizing them. Why?" %}
{% assign hrefs = hrefs | push: "import" %}
{% assign descriptions = descriptions | push: "The main way to import cards via CSV is using the Helvault format, which contains the following columns: <code>extras</code>, <code>name</code>, <code>scryfall_id</code>, <code>quantity</code>.<br/><br/>You can also use other PRO formats such as Plain List, TCG Player, Deckbox, and many others after purchasing the 'PRO Import and Export' feature." %}


{% assign titles = titles | push: "I'm trying to export my cards via CSV to another app/website but they don't recognize it. What can I do?" %}
{% assign hrefs = hrefs | push: "export" %}
{% assign descriptions = descriptions | push: "There is no unified CSV format for card import/export, so each app uses its own. Here are some suggestions:<br/><br/>1. Edit the headers of the CSV file on your computer. The other service might expect <code>card_name</code> instead of <code>name</code>, for example.<br/>2. Contact them to ask about their expected CSV format if you don't already know it.<br/>3. If you need additional columns in your CSV file such as <code>price</code>, <code>set code</code>, <code>set name</code>, or <code>oracle id</code>, take a look at the 'Helvault PRO CSV' format. It's a one-time purchase (not a subscription) that may help you." %}


{% assign titles = titles | push: "How does iCloud Sync work?" %}
{% assign hrefs = hrefs | push: "icloud" %}
{% assign descriptions = descriptions | push: "When you enable iCloud Sync by purchasing the 'iCloud Sync' feature, you'll leverage the power of iCloud to have all your content (such as cards, binders, lists, and prices) synchronized between your devices.<br/><br/>Keep in mind that larger changes take longer to sync. For instance, if you add a new card on device 'A', you should see it on device 'B' almost instantly. However, if you import 1,000 cards via CSV, it might take a while for them to appear on all devices.<br/><br/>You can check the iCloud Sync status of your device by doing the following:<br/><br/>1. Open the Helvault app<br/>2. In the 'Collections' area, go to Settings (three-dotted button in the top left corner)<br/>3. Scroll down and tap 'iCloud Syncing'" %}


{% assign titles = titles | push: "iCloud Sync is taking too long. What's going on?" %}
{% assign hrefs = hrefs | push: "icloudThrottle" %}
{% assign descriptions = descriptions | push: "When you import a large amount of data at once (such as a long CSV file or a backup from the Legacy app), iCloud will automatically throttle the data transfer rate to preserve their server stability. Unfortunately, this is not something Helvault can control—all apps (including Apple's own) are affected by this. Additionally, completion time is not linear, so the more you sync at once, the longer it will take.<br/><br/>Here are some rough estimates as a guide:<br/><br/>- 500 cards should finish uploading almost instantly<br/>- 3,000 cards should finish uploading in about 5 minutes<br/>- 14,000 cards should finish uploading in about 4.5 hours<br/><br/>Keep in mind that these numbers may vary considerably depending on factors such as iCloud server availability, your internet connection speed, and your physical distance to iCloud servers." %}


{% assign titles = titles | push: "iCloud Sync isn't working. What can I do?" %}
{% assign hrefs = hrefs | push: "icloudFix" %}
{% assign descriptions = descriptions | push: "If you have purchased the 'iCloud Sync' feature and suspect that content is not syncing properly between devices, here are some things you can try:<br/><br/>1. Verify that you are signed in to iCloud on your device. More details <a href='https://support.apple.com/en-gb/guide/icloud/mmfc0f1e2a/1.0/icloud/1.0' target='_blank'>here</a>.<br/>2. Within the app, go to <code>Settings → iCloud Syncing</code> and check that <code>iCloud Account</code> displays as <code>Available</code> and <code>Setup</code> displays as <code>Successful</code>. If either shows something different, check step 1 above.<br/>3. Make sure Helvault has permission to use iCloud. Go to <code>Settings → [your name] → iCloud → Show All (under the APPS USING ICLOUD section)</code>. On this page, the toggle should be turned ON for Helvault. If you cannot reach this page, check step 1 above." %}

<div class="faq-body">
  {% for i in (1..titles.size) %}
  {% assign index = i | minus: 1 %}
    <div class="faq-collapse-item">
      <a class="faq-collapse-btn" data-bs-toggle="collapse" href="#{{ hrefs[index] }}">{{ titles[index] }}</a>
      <div class="faq-collapse-content collapse" id="{{ hrefs[index] }}"><br/>{{ descriptions[index] }}</div>
    </div>
  {% endfor %}
</div>
