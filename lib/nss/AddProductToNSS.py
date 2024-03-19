import requests
import json

class AddProductToNSS:
    def __init__(self, telephoneNumber, bearer_token, name, leafCategoryId, imageUrl, salePrice, importer, sellerBarcode, productInfoProvidedNoticeType, html_content):
        self.telephoneNumber = telephoneNumber
        self.bearer_token = bearer_token
        self.name = name
        self.leafCategoryId = leafCategoryId
        self.imageUrl = imageUrl
        self.salePrice = salePrice
        self.importer = importer
        self.sellerBarcode = sellerBarcode
        self.productInfoProvidedNoticeType = productInfoProvidedNoticeType
        self.html_content = html_content

    def add_product(self):
        url = "https://api.commerce.naver.com/external/v2/products"

        data = {
            "originProduct": {
                "statusType": "SALE",
                "saleType": "NEW",
                "leafCategoryId": self.leafCategoryId,
                "name": self.name,
                "detailContent": self.html_content,
                "images": {
                    "representativeImage": {
                        "url": self.imageUrl
                    },
                },
                "salePrice": self.salePrice,
                "stockQuantity": 100,
                "deliveryInfo": {
                    "deliveryType": "DELIVERY",
                    "deliveryAttributeType": "NORMAL",
                    "deliveryCompany": "HANJIN",
                    "deliveryFee": {
                        "deliveryFeeType": "FREE",
                    },
                    "claimDeliveryInfo": {
                        "returnDeliveryFee": 50000,
                        "exchangeDeliveryFee": 100000
                    }
                },
                "detailAttribute": {
                    "afterServiceInfo": {
                        "afterServiceTelephoneNumber": self.telephoneNumber,
                        "afterServiceGuideContent": "고객님의 부주의로 파손이 됐을 경우 A/S비용이 청구될 수도 있습니다."
                    },
                    "originAreaInfo": {
                        "originAreaCode": "0204000",
                        "importer": self.importer,
                    },
                    "minorPurchasable": True,
                    "productInfoProvidedNotice": {
                        "productInfoProvidedNoticeType": self.productInfoProvidedNoticeType,
                        self.productInfoProvidedNoticeType: {
                            "returnCostReason": "",
                            "noRefundReason": "",
                            "qualityAssuranceStandard": "",
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
                        , "sellerBarcode": self.sellerBarcode
                    },
                    "certificationTargetExcludeContent": {
                        "kcExemptionType": "OVERSEAS",
                        "kcCertifiedProductExclusionYn": "KC_EXEMPTION_OBJECT"
                    }
                },
            },
            "smartstoreChannelProduct": {
                "naverShoppingRegistration": True,
                "channelProductDisplayStatusType": "WAIT"
            }
        }

        # 요청 헤더
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.bearer_token
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))

        # 응답 확인
        if response.status_code == 200:
            # 성공적인 응답 처리
            print("성공:", response.json())
        else:
            # 오류 응답 처리
            print("오류:", response.status_code, response.text)