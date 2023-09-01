---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

_Senior iOS Engineer touching people's lives through technology since 2010._

## Resume
You can find below my resume with an overview of my professional experience.

[<i class="fas fa-download"></i> Get a Copy]({{site.resume_path}})

<html>
<style>
	.resume-container {}

	.resume-deafult-container {
		display: none;
	}

	.resume-embed {
		width: 100%;
		height: 1000px;
	}

	.resume-default-icon {
		font-size: 48px;
		margin-left: calc(50% - 24px);
		margin-top: 20px;
	}

	.resume-default-message {
		text-align: center;
	}

	@media only screen and (max-width: 620px) {
		.resume-container {
			display: none;
		}

		.resume-deafult-container {
			display: block;
		}
	}
</style>

<body>
	<div class="resume-container">
		<object class="resume-embed" type="application/pdf" data="..{{site.resume_path}}">
			<br />
			<p>
				<br />
				It appears that your browser cannot display the PDF correctly. Please get a copy by clicking the link above.
				<br />
			</p>
			<br />
		</object>
		<br />
	</div>
	<br />
	<br />
	<div class="resume-deafult-container">
		<br />
		<i class="fas fa-rocket resume-default-icon"></i>
		<br />
		<p class="resume-default-message">
			<br />
			PDF display in mobile devices is not implemented yet. Please get a copy by tapping the link above.
			<br />
		</p>
		<br />
	</div>
</body>

</html>