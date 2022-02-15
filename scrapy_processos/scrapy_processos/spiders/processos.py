import scrapy

class ProcessosSpider(scrapy.Spider):
    #nome do spider
    name = "processos"
 #lista de urls para raspagem
    start_urls = [
        "https://cp.trf5.jus.br/processo/00156487819994050000",
        "https://cp.trf5.jus.br/processo/00126569020124050000",
        "https://cp.trf5.jus.br/processo/00437537420134050000",
        "https://cp.trf5.jus.br/processo/00020980720114058500",
        "https://cp.trf5.jus.br/processo/04606743320194050000",
        "https://cp.trf5.jus.br/processo/00005606720174050000"

    ]
    #função de raspagem da pagina html
    def parse(self, response):
        for processo in response.css('body.ff'):
            yield {
                "numero_processo": processo.css('br+ p::text').extract_first(),
                "nª_legado": processo.css('p+ p::text').extract_first(),
                "data_autuacao": processo.css('div.right::text').extract_first(),



            }