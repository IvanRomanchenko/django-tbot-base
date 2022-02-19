import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="django-tbot-base",
	version="1.0.0",
	author="Ivan Romanchenko",
	author_email="vanvanych789@gmail.com",
	description="Django Telegram bot base config",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/IvanRomanchenko/django-tbot-base",
	packages=["tbot_base", ],
	include_package_data=True,
	classifiers=[
		"Programming Language :: Python :: 3.10",
		"Framework :: Django :: 4.0",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.6",
	install_requires=[
		"Django==4.0.2",
		"pyTelegramBotAPI==4.4.0",
		"loguru==0.6.0",
	]
)
