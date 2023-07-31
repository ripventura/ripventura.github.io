---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---
<html>
	<head><link rel="stylesheet" href="style.css"></head>
</html>

# FAQ
Below you'll find answers to common questions you may have about Helvault. If you need extra support consider [reaching us out]({{site.helvault_support_form}}) or [joining our Discord server](https://discord.gg/WMWNpmcg35).

{% assign titles = "" | split: "" %}
{% assign descriptions = "" | split: "" %}


{% assign titles = titles | push: "Why the need for a new Helvault?" %}
{% assign descriptions = descriptions | push: "We appreciate the support and would like to clarify the reasons behind the creation of the new Helvault.<br/>First of all, we understand how depreciative a subscription based model is to its users, that is why we do not (and will never) implement recurring subscriptions on the app. However, development of new features + maintenance takes time and money. We needed a way to keep new stuff coming in without abusing users with recurring charges.<br/><br/>That is the reason we decided to create a new app from scratch, more solid and modern, that will be the foundation for the upcoming years.<br/>In short, if you want new stuff and would like to support the development of this indie app, the new Helvault is here for you! Otherwise keep using the old app and no hard feelings." %}

{% assign titles = titles | push: "Will the old Helvault stop working?" %}
{% assign descriptions = descriptions | push: "No! The app will continue to work normally. The only change is that it will no longer receive updates." %}


{% assign titles = titles | push: "I'm trying to import my cards via CSV but the app is not recognizing them... Why?" %}
{% assign descriptions = descriptions | push: "The may way of importing cards via CSV is using the Helvault format, which contains the following columns: extras, name, scryfall_id, quantity.<br/>You can also use other PRO formats such as Plain List, TCG Player, Deckbox and many others after purchasing the PRO Import and Export package." %}


{% assign titles = titles | push: "I'm trying to export my cards via CSV into another app/website but they don't recognize it... What can I do?" %}
{% assign descriptions = descriptions | push: "There is no unified CSV format for card import/export, so each app prefer its own... Here are some suggestions on what you can do to import cards in other services:<br/><br/>1. Edit the headers of the CSV file on your computer... Maybe they expect <i>card_name</i> instead of <i>name</i>.<br/>2. Reach them out asking for expected CSV formats if you don't already know.<br/>3. If you need more columns on your CSV file such as <i>price, set code, set name, oracle id</i> etc, take a look at the Helvault PRO CSV format. It's a single-purchase (not a subscription) that may help you." %}


{% assign titles = titles | push: "I already bought the Scanner and now the app is showing other features available to purchase... Why?" %}
{% assign descriptions = descriptions | push: "Helvault is split in segments of 'PRO' features. They are one time purchases (<b>not</b> subscriptions) that will unlock more content for users who believe they are worth it." %}

{% for i in (1..titles.size) %}
{% assign index = i | minus: 1 %}
  <h2>{{ i }}. {{ titles[index] }}</h2>
  {{ descriptions[index] }}
{% endfor %}