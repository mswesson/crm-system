from django.core.management import BaseCommand

from services.models import Service
from advertising.models import AdvertisingCompany


class Command(BaseCommand):
    """Creates advertising"""

    def handle(self, *args, **options):
        self.stdout.write("Start of advertising creation")

        advertising_data = [
            {
                "title": "Website Development Special Offer",
                "promotion_channel": "Google Ads",
                "budget": 1500,
                "service_id": 1,
            },
            {
                "title": "Mobile App Launch Campaign",
                "promotion_channel": "Facebook Ads",
                "budget": 2000,
                "service_id": 2,
            },
            {
                "title": "Boost Your Online Visibility - SEO",
                "promotion_channel": "Google Search Ads",
                "budget": 1000,
                "service_id": 3,
            },
            {
                "title": "IT Consulting - Digital Transformation",
                "promotion_channel": "LinkedIn Ads",
                "budget": 1200,
                "service_id": 4,
            },
            {
                "title": "Enhance Your Business with Custom Software",
                "promotion_channel": "Instagram Ads",
                "budget": 1800,
                "service_id": 5,
            },
            {
                "title": "Cloud Solutions for Scalability",
                "promotion_channel": "Twitter Ads",
                "budget": 1400,
                "service_id": 6,
            },
            {
                "title": "Secure Your Business - Cybersecurity",
                "promotion_channel": "Google Display Network",
                "budget": 1600,
                "service_id": 7,
            },
            {
                "title": "Get a CRM System for Better Sales",
                "promotion_channel": "Facebook Ads",
                "budget": 1500,
                "service_id": 8,
            },
            {
                "title": "Optimize Your IT Infrastructure",
                "promotion_channel": "LinkedIn Ads",
                "budget": 1300,
                "service_id": 9,
            },
            {
                "title": "Third-party Service Integration Promo",
                "promotion_channel": "Twitter Ads",
                "budget": 1100,
                "service_id": 10,
            },
            {
                "title": "Mobile App Development for Your Business",
                "promotion_channel": "Google Ads",
                "budget": 2000,
                "service_id": 2,
            },
            {
                "title": "Website Development for Small Businesses",
                "promotion_channel": "Instagram Ads",
                "budget": 1000,
                "service_id": 1,
            },
            {
                "title": "IT Infrastructure Support Campaign",
                "promotion_channel": "LinkedIn Ads",
                "budget": 1700,
                "service_id": 9,
            },
            {
                "title": "Boost Your Sales with Custom Software",
                "promotion_channel": "Facebook Ads",
                "budget": 1600,
                "service_id": 5,
            },
            {
                "title": "Cloud Solutions for Remote Work",
                "promotion_channel": "Google Search Ads",
                "budget": 1300,
                "service_id": 6,
            },
        ]

        services = Service.objects.all()

        for adv_data in advertising_data:

            try:
                service = services.get(pk=adv_data["service_id"])
            except Service.DoesNotExist:
                self.stdout.write("The services were not created in advance")
                return

            advertising, create = AdvertisingCompany.objects.get_or_create(
                title=adv_data["title"],
                promotion_channel=adv_data["promotion_channel"],
                budget=adv_data["budget"],
                service=service,
            )

            self.stdout.write(f"Created advertising: {advertising.title}")

        self.stdout.write(self.style.SUCCESS("Advertising created"))
