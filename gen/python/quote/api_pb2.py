# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: quote/api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fquote/api.proto\x12\x14longportapp.quote.v1\")\n\x0fSecurityRequest\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\".\n\x14MultiSecurityRequest\x12\x16\n\x06symbol\x18\x01 \x03(\tR\x06symbol\"h\n\x1aSecurityStaticInfoResponse\x12J\n\x10secu_static_info\x18\x01 \x03(\x0b\x32 .longportapp.quote.v1.StaticInfoR\x0esecuStaticInfo\"\xfb\x03\n\nStaticInfo\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x17\n\x07name_cn\x18\x02 \x01(\tR\x06nameCn\x12\x17\n\x07name_en\x18\x03 \x01(\tR\x06nameEn\x12\x17\n\x07name_hk\x18\x04 \x01(\tR\x06nameHk\x12!\n\x0clisting_date\x18\x05 \x01(\tR\x0blistingDate\x12\x1a\n\x08\x65xchange\x18\x06 \x01(\tR\x08\x65xchange\x12\x1a\n\x08\x63urrency\x18\x07 \x01(\tR\x08\x63urrency\x12\x19\n\x08lot_size\x18\x08 \x01(\x05R\x07lotSize\x12!\n\x0ctotal_shares\x18\t \x01(\x03R\x0btotalShares\x12-\n\x12\x63irculating_shares\x18\n \x01(\x03R\x11\x63irculatingShares\x12\x1b\n\thk_shares\x18\x0b \x01(\x03R\x08hkShares\x12\x10\n\x03\x65ps\x18\x0c \x01(\tR\x03\x65ps\x12\x17\n\x07\x65ps_ttm\x18\r \x01(\tR\x06\x65psTtm\x12\x10\n\x03\x62ps\x18\x0e \x01(\tR\x03\x62ps\x12%\n\x0e\x64ividend_yield\x18\x0f \x01(\tR\rdividendYield\x12+\n\x11stock_derivatives\x18\x10 \x03(\x05R\x10stockDerivatives\x12\x14\n\x05\x62oard\x18\x11 \x01(\tR\x05\x62oard\"[\n\x15SecurityQuoteResponse\x12\x42\n\nsecu_quote\x18\x01 \x03(\x0b\x32#.longportapp.quote.v1.SecurityQuoteR\tsecuQuote\"\xd3\x03\n\rSecurityQuote\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x1b\n\tlast_done\x18\x02 \x01(\tR\x08lastDone\x12\x1d\n\nprev_close\x18\x03 \x01(\tR\tprevClose\x12\x12\n\x04open\x18\x04 \x01(\tR\x04open\x12\x12\n\x04high\x18\x05 \x01(\tR\x04high\x12\x10\n\x03low\x18\x06 \x01(\tR\x03low\x12\x1c\n\ttimestamp\x18\x07 \x01(\x03R\ttimestamp\x12\x16\n\x06volume\x18\x08 \x01(\x03R\x06volume\x12\x1a\n\x08turnover\x18\t \x01(\tR\x08turnover\x12\x44\n\x0ctrade_status\x18\n \x01(\x0e\x32!.longportapp.quote.v1.TradeStatusR\x0btradeStatus\x12L\n\x10pre_market_quote\x18\x0b \x01(\x0b\x32\".longportapp.quote.v1.PrePostQuoteR\x0epreMarketQuote\x12N\n\x11post_market_quote\x18\x0c \x01(\x0b\x32\".longportapp.quote.v1.PrePostQuoteR\x0fpostMarketQuote\"\xc2\x01\n\x0cPrePostQuote\x12\x1b\n\tlast_done\x18\x01 \x01(\tR\x08lastDone\x12\x1c\n\ttimestamp\x18\x02 \x01(\x03R\ttimestamp\x12\x16\n\x06volume\x18\x03 \x01(\x03R\x06volume\x12\x1a\n\x08turnover\x18\x04 \x01(\tR\x08turnover\x12\x12\n\x04high\x18\x05 \x01(\tR\x04high\x12\x10\n\x03low\x18\x06 \x01(\tR\x03low\x12\x1d\n\nprev_close\x18\x07 \x01(\tR\tprevClose\"W\n\x13OptionQuoteResponse\x12@\n\nsecu_quote\x18\x01 \x03(\x0b\x32!.longportapp.quote.v1.OptionQuoteR\tsecuQuote\"\xfc\x02\n\x0bOptionQuote\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x1b\n\tlast_done\x18\x02 \x01(\tR\x08lastDone\x12\x1d\n\nprev_close\x18\x03 \x01(\tR\tprevClose\x12\x12\n\x04open\x18\x04 \x01(\tR\x04open\x12\x12\n\x04high\x18\x05 \x01(\tR\x04high\x12\x10\n\x03low\x18\x06 \x01(\tR\x03low\x12\x1c\n\ttimestamp\x18\x07 \x01(\x03R\ttimestamp\x12\x16\n\x06volume\x18\x08 \x01(\x03R\x06volume\x12\x1a\n\x08turnover\x18\t \x01(\tR\x08turnover\x12\x44\n\x0ctrade_status\x18\n \x01(\x0e\x32!.longportapp.quote.v1.TradeStatusR\x0btradeStatus\x12G\n\roption_extend\x18\x0b \x01(\x0b\x32\".longportapp.quote.v1.OptionExtendR\x0coptionExtend\"\xa1\x03\n\x0cOptionExtend\x12-\n\x12implied_volatility\x18\x01 \x01(\tR\x11impliedVolatility\x12#\n\ropen_interest\x18\x02 \x01(\x03R\x0copenInterest\x12\x1f\n\x0b\x65xpiry_date\x18\x03 \x01(\tR\nexpiryDate\x12!\n\x0cstrike_price\x18\x04 \x01(\tR\x0bstrikePrice\x12/\n\x13\x63ontract_multiplier\x18\x05 \x01(\tR\x12\x63ontractMultiplier\x12#\n\rcontract_type\x18\x06 \x01(\tR\x0c\x63ontractType\x12#\n\rcontract_size\x18\x07 \x01(\tR\x0c\x63ontractSize\x12\x1c\n\tdirection\x18\x08 \x01(\tR\tdirection\x12\x33\n\x15historical_volatility\x18\t \x01(\tR\x14historicalVolatility\x12+\n\x11underlying_symbol\x18\n \x01(\tR\x10underlyingSymbol\"Y\n\x14WarrantQuoteResponse\x12\x41\n\nsecu_quote\x18\x02 \x03(\x0b\x32\".longportapp.quote.v1.WarrantQuoteR\tsecuQuote\"\x80\x03\n\x0cWarrantQuote\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x1b\n\tlast_done\x18\x02 \x01(\tR\x08lastDone\x12\x1d\n\nprev_close\x18\x03 \x01(\tR\tprevClose\x12\x12\n\x04open\x18\x04 \x01(\tR\x04open\x12\x12\n\x04high\x18\x05 \x01(\tR\x04high\x12\x10\n\x03low\x18\x06 \x01(\tR\x03low\x12\x1c\n\ttimestamp\x18\x07 \x01(\x03R\ttimestamp\x12\x16\n\x06volume\x18\x08 \x01(\x03R\x06volume\x12\x1a\n\x08turnover\x18\t \x01(\tR\x08turnover\x12\x44\n\x0ctrade_status\x18\n \x01(\x0e\x32!.longportapp.quote.v1.TradeStatusR\x0btradeStatus\x12J\n\x0ewarrant_extend\x18\x0b \x01(\x0b\x32#.longportapp.quote.v1.WarrantExtendR\rwarrantExtend\"\xef\x03\n\rWarrantExtend\x12-\n\x12implied_volatility\x18\x01 \x01(\tR\x11impliedVolatility\x12\x1f\n\x0b\x65xpiry_date\x18\x02 \x01(\tR\nexpiryDate\x12&\n\x0flast_trade_date\x18\x03 \x01(\tR\rlastTradeDate\x12+\n\x11outstanding_ratio\x18\x04 \x01(\tR\x10outstandingRatio\x12\'\n\x0foutstanding_qty\x18\x05 \x01(\x03R\x0eoutstandingQty\x12)\n\x10\x63onversion_ratio\x18\x06 \x01(\tR\x0f\x63onversionRatio\x12\x1a\n\x08\x63\x61tegory\x18\x07 \x01(\tR\x08\x63\x61tegory\x12!\n\x0cstrike_price\x18\x08 \x01(\tR\x0bstrikePrice\x12,\n\x12upper_strike_price\x18\t \x01(\tR\x10upperStrikePrice\x12,\n\x12lower_strike_price\x18\n \x01(\tR\x10lowerStrikePrice\x12\x1d\n\ncall_price\x18\x0b \x01(\tR\tcallPrice\x12+\n\x11underlying_symbol\x18\x0c \x01(\tR\x10underlyingSymbol\"\x8d\x01\n\x15SecurityDepthResponse\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12-\n\x03\x61sk\x18\x02 \x03(\x0b\x32\x1b.longportapp.quote.v1.DepthR\x03\x61sk\x12-\n\x03\x62id\x18\x03 \x03(\x0b\x32\x1b.longportapp.quote.v1.DepthR\x03\x62id\"n\n\x05\x44\x65pth\x12\x1a\n\x08position\x18\x01 \x01(\x05R\x08position\x12\x14\n\x05price\x18\x02 \x01(\tR\x05price\x12\x16\n\x06volume\x18\x03 \x01(\x03R\x06volume\x12\x1b\n\torder_num\x18\x04 \x01(\x03R\x08orderNum\"\xb1\x01\n\x17SecurityBrokersResponse\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12>\n\x0b\x61sk_brokers\x18\x02 \x03(\x0b\x32\x1d.longportapp.quote.v1.BrokersR\naskBrokers\x12>\n\x0b\x62id_brokers\x18\x03 \x03(\x0b\x32\x1d.longportapp.quote.v1.BrokersR\nbidBrokers\"D\n\x07\x42rokers\x12\x1a\n\x08position\x18\x01 \x01(\x05R\x08position\x12\x1d\n\nbroker_ids\x18\x02 \x03(\x05R\tbrokerIds\"\x83\x01\n\x1cParticipantBrokerIdsResponse\x12\x63\n\x1aparticipant_broker_numbers\x18\x01 \x03(\x0b\x32%.longportapp.quote.v1.ParticipantInfoR\x18participantBrokerNumbers\"\xc0\x01\n\x0fParticipantInfo\x12\x1d\n\nbroker_ids\x18\x01 \x03(\x05R\tbrokerIds\x12.\n\x13participant_name_cn\x18\x02 \x01(\tR\x11participantNameCn\x12.\n\x13participant_name_en\x18\x03 \x01(\tR\x11participantNameEn\x12.\n\x13participant_name_hk\x18\x04 \x01(\tR\x11participantNameHk\"D\n\x14SecurityTradeRequest\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x14\n\x05\x63ount\x18\x02 \x01(\x05R\x05\x63ount\"d\n\x15SecurityTradeResponse\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x33\n\x06trades\x18\x02 \x03(\x0b\x32\x1b.longportapp.quote.v1.TradeR\x06trades\"\xd9\x01\n\x05Trade\x12\x14\n\x05price\x18\x01 \x01(\tR\x05price\x12\x16\n\x06volume\x18\x02 \x01(\x03R\x06volume\x12\x1c\n\ttimestamp\x18\x03 \x01(\x03R\ttimestamp\x12\x1d\n\ntrade_type\x18\x04 \x01(\tR\ttradeType\x12\x1c\n\tdirection\x18\x05 \x01(\x05R\tdirection\x12G\n\rtrade_session\x18\x06 \x01(\x0e\x32\".longportapp.quote.v1.TradeSessionR\x0ctradeSession\"1\n\x17SecurityIntradayRequest\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\"d\n\x18SecurityIntradayResponse\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x30\n\x05lines\x18\x02 \x03(\x0b\x32\x1a.longportapp.quote.v1.LineR\x05lines\"\x8b\x01\n\x04Line\x12\x14\n\x05price\x18\x01 \x01(\tR\x05price\x12\x1c\n\ttimestamp\x18\x02 \x01(\x03R\ttimestamp\x12\x16\n\x06volume\x18\x03 \x01(\x03R\x06volume\x12\x1a\n\x08turnover\x18\x04 \x01(\tR\x08turnover\x12\x1b\n\tavg_price\x18\x05 \x01(\tR\x08\x61vgPrice\"\xc3\x01\n\x1aSecurityCandlestickRequest\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x34\n\x06period\x18\x02 \x01(\x0e\x32\x1c.longportapp.quote.v1.PeriodR\x06period\x12\x14\n\x05\x63ount\x18\x03 \x01(\x05R\x05\x63ount\x12\x41\n\x0b\x61\x64just_type\x18\x04 \x01(\x0e\x32 .longportapp.quote.v1.AdjustTypeR\nadjustType\"|\n\x1bSecurityCandlestickResponse\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x45\n\x0c\x63\x61ndlesticks\x18\x02 \x03(\x0b\x32!.longportapp.quote.v1.CandlestickR\x0c\x63\x61ndlesticks\"\xaf\x01\n\x0b\x43\x61ndlestick\x12\x14\n\x05\x63lose\x18\x01 \x01(\tR\x05\x63lose\x12\x12\n\x04open\x18\x02 \x01(\tR\x04open\x12\x10\n\x03low\x18\x03 \x01(\tR\x03low\x12\x12\n\x04high\x18\x04 \x01(\tR\x04high\x12\x16\n\x06volume\x18\x05 \x01(\x03R\x06volume\x12\x1a\n\x08turnover\x18\x06 \x01(\tR\x08turnover\x12\x1c\n\ttimestamp\x18\x07 \x01(\x03R\ttimestamp\">\n\x1bOptionChainDateListResponse\x12\x1f\n\x0b\x65xpiry_date\x18\x01 \x03(\tR\nexpiryDate\"[\n OptionChainDateStrikeInfoRequest\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x1f\n\x0b\x65xpiry_date\x18\x02 \x01(\tR\nexpiryDate\"v\n!OptionChainDateStrikeInfoResponse\x12Q\n\x11strike_price_info\x18\x01 \x03(\x0b\x32%.longportapp.quote.v1.StrikePriceInfoR\x0fstrikePriceInfo\"\x83\x01\n\x0fStrikePriceInfo\x12\x14\n\x05price\x18\x01 \x01(\tR\x05price\x12\x1f\n\x0b\x63\x61ll_symbol\x18\x02 \x01(\tR\ncallSymbol\x12\x1d\n\nput_symbol\x18\x03 \x01(\tR\tputSymbol\x12\x1a\n\x08standard\x18\x04 \x01(\x08R\x08standard\"W\n\x12IssuerInfoResponse\x12\x41\n\x0bissuer_info\x18\x01 \x03(\x0b\x32 .longportapp.quote.v1.IssuerInfoR\nissuerInfo\"g\n\nIssuerInfo\x12\x0e\n\x02id\x18\x01 \x01(\x05R\x02id\x12\x17\n\x07name_cn\x18\x02 \x01(\tR\x06nameCn\x12\x17\n\x07name_en\x18\x03 \x01(\tR\x06nameEn\x12\x17\n\x07name_hk\x18\x04 \x01(\tR\x06nameHk\"\x97\x01\n\x18WarrantFilterListRequest\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12G\n\rfilter_config\x18\x02 \x01(\x0b\x32\".longportapp.quote.v1.FilterConfigR\x0c\x66ilterConfig\x12\x1a\n\x08language\x18\x03 \x01(\x05R\x08language\"\x8a\x02\n\x0c\x46ilterConfig\x12\x17\n\x07sort_by\x18\x01 \x01(\x05R\x06sortBy\x12\x1d\n\nsort_order\x18\x02 \x01(\x05R\tsortOrder\x12\x1f\n\x0bsort_offset\x18\x03 \x01(\x05R\nsortOffset\x12\x1d\n\nsort_count\x18\x04 \x01(\x05R\tsortCount\x12\x12\n\x04type\x18\x05 \x03(\x05R\x04type\x12\x16\n\x06issuer\x18\x06 \x03(\x05R\x06issuer\x12\x1f\n\x0b\x65xpiry_date\x18\x07 \x03(\x05R\nexpiryDate\x12\x1d\n\nprice_type\x18\x08 \x03(\x05R\tpriceType\x12\x16\n\x06status\x18\t \x03(\x05R\x06status\"\x84\x01\n\x19WarrantFilterListResponse\x12\x46\n\x0cwarrant_list\x18\x01 \x03(\x0b\x32#.longportapp.quote.v1.FilterWarrantR\x0bwarrantList\x12\x1f\n\x0btotal_count\x18\x02 \x01(\x05R\ntotalCount\"\xcf\x06\n\rFilterWarrant\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1b\n\tlast_done\x18\x03 \x01(\tR\x08lastDone\x12\x1f\n\x0b\x63hange_rate\x18\x04 \x01(\tR\nchangeRate\x12\x1d\n\nchange_val\x18\x05 \x01(\tR\tchangeVal\x12\x16\n\x06volume\x18\x06 \x01(\x03R\x06volume\x12\x1a\n\x08turnover\x18\x07 \x01(\tR\x08turnover\x12\x1f\n\x0b\x65xpiry_date\x18\x08 \x01(\tR\nexpiryDate\x12!\n\x0cstrike_price\x18\t \x01(\tR\x0bstrikePrice\x12,\n\x12upper_strike_price\x18\n \x01(\tR\x10upperStrikePrice\x12,\n\x12lower_strike_price\x18\x0b \x01(\tR\x10lowerStrikePrice\x12\'\n\x0foutstanding_qty\x18\x0c \x01(\tR\x0eoutstandingQty\x12+\n\x11outstanding_ratio\x18\r \x01(\tR\x10outstandingRatio\x12\x18\n\x07premium\x18\x0e \x01(\tR\x07premium\x12\x17\n\x07itm_otm\x18\x0f \x01(\tR\x06itmOtm\x12-\n\x12implied_volatility\x18\x10 \x01(\tR\x11impliedVolatility\x12\x14\n\x05\x64\x65lta\x18\x11 \x01(\tR\x05\x64\x65lta\x12\x1d\n\ncall_price\x18\x12 \x01(\tR\tcallPrice\x12\"\n\rto_call_price\x18\x13 \x01(\tR\x0btoCallPrice\x12-\n\x12\x65\x66\x66\x65\x63tive_leverage\x18\x14 \x01(\tR\x11\x65\x66\x66\x65\x63tiveLeverage\x12%\n\x0eleverage_ratio\x18\x15 \x01(\tR\rleverageRatio\x12)\n\x10\x63onversion_ratio\x18\x16 \x01(\tR\x0f\x63onversionRatio\x12#\n\rbalance_point\x18\x17 \x01(\tR\x0c\x62\x61lancePoint\x12\x16\n\x06status\x18\x18 \x01(\x05R\x06status\x12\x12\n\x04type\x18\x19 \x01(\x05R\x04type\"v\n\x19MarketTradePeriodResponse\x12Y\n\x14market_trade_session\x18\x01 \x03(\x0b\x32\'.longportapp.quote.v1.MarketTradePeriodR\x12marketTradeSession\"s\n\x11MarketTradePeriod\x12\x16\n\x06market\x18\x01 \x01(\tR\x06market\x12\x46\n\rtrade_session\x18\x02 \x03(\x0b\x32!.longportapp.quote.v1.TradePeriodR\x0ctradeSession\"\x8c\x01\n\x0bTradePeriod\x12\x19\n\x08\x62\x65g_time\x18\x01 \x01(\x05R\x07\x62\x65gTime\x12\x19\n\x08\x65nd_time\x18\x02 \x01(\x05R\x07\x65ndTime\x12G\n\rtrade_session\x18\x03 \x01(\x0e\x32\".longportapp.quote.v1.TradeSessionR\x0ctradeSession\"\x15\n\x13SubscriptionRequest\"T\n\x14SubscriptionResponse\x12<\n\x08sub_list\x18\x01 \x03(\x0b\x32!.longportapp.quote.v1.SubTypeListR\x07subList\"_\n\x0bSubTypeList\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x38\n\x08sub_type\x18\x02 \x03(\x0e\x32\x1d.longportapp.quote.v1.SubTypeR\x07subType\"\x88\x01\n\x10SubscribeRequest\x12\x16\n\x06symbol\x18\x01 \x03(\tR\x06symbol\x12\x38\n\x08sub_type\x18\x02 \x03(\x0e\x32\x1d.longportapp.quote.v1.SubTypeR\x07subType\x12\"\n\ris_first_push\x18\x03 \x01(\x08R\x0bisFirstPush\"\x83\x01\n\x12UnsubscribeRequest\x12\x16\n\x06symbol\x18\x01 \x03(\tR\x06symbol\x12\x38\n\x08sub_type\x18\x02 \x03(\x0e\x32\x1d.longportapp.quote.v1.SubTypeR\x07subType\x12\x1b\n\tunsub_all\x18\x03 \x01(\x08R\x08unsubAll\"\x15\n\x13UnsubscribeResponse\"\xff\x03\n\tPushQuote\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x1a\n\x08sequence\x18\x02 \x01(\x03R\x08sequence\x12\x1b\n\tlast_done\x18\x03 \x01(\tR\x08lastDone\x12\x12\n\x04open\x18\x04 \x01(\tR\x04open\x12\x12\n\x04high\x18\x05 \x01(\tR\x04high\x12\x10\n\x03low\x18\x06 \x01(\tR\x03low\x12\x1c\n\ttimestamp\x18\x07 \x01(\x03R\ttimestamp\x12\x16\n\x06volume\x18\x08 \x01(\x03R\x06volume\x12\x1a\n\x08turnover\x18\t \x01(\tR\x08turnover\x12\x44\n\x0ctrade_status\x18\n \x01(\x0e\x32!.longportapp.quote.v1.TradeStatusR\x0btradeStatus\x12G\n\rtrade_session\x18\x0b \x01(\x0e\x32\".longportapp.quote.v1.TradeSessionR\x0ctradeSession\x12%\n\x0e\x63urrent_volume\x18\x0c \x01(\x03R\rcurrentVolume\x12)\n\x10\x63urrent_turnover\x18\r \x01(\tR\x0f\x63urrentTurnover\x12\x34\n\x03tag\x18\x0e \x01(\x0e\x32\".longportapp.quote.v1.PushQuoteTagR\x03tag\"\x9d\x01\n\tPushDepth\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x1a\n\x08sequence\x18\x02 \x01(\x03R\x08sequence\x12-\n\x03\x61sk\x18\x03 \x03(\x0b\x32\x1b.longportapp.quote.v1.DepthR\x03\x61sk\x12-\n\x03\x62id\x18\x04 \x03(\x0b\x32\x1b.longportapp.quote.v1.DepthR\x03\x62id\"\xc1\x01\n\x0bPushBrokers\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x1a\n\x08sequence\x18\x02 \x01(\x03R\x08sequence\x12>\n\x0b\x61sk_brokers\x18\x03 \x03(\x0b\x32\x1d.longportapp.quote.v1.BrokersR\naskBrokers\x12>\n\x0b\x62id_brokers\x18\x04 \x03(\x0b\x32\x1d.longportapp.quote.v1.BrokersR\nbidBrokers\"r\n\tPushTrade\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x1a\n\x08sequence\x18\x02 \x01(\x03R\x08sequence\x12\x31\n\x05trade\x18\x03 \x03(\x0b\x32\x1b.longportapp.quote.v1.TradeR\x05trade\"a\n\x15MarketTradeDayRequest\x12\x16\n\x06market\x18\x01 \x01(\tR\x06market\x12\x17\n\x07\x62\x65g_day\x18\x02 \x01(\tR\x06\x62\x65gDay\x12\x17\n\x07\x65nd_day\x18\x03 \x01(\tR\x06\x65ndDay\"[\n\x16MarketTradeDayResponse\x12\x1b\n\ttrade_day\x18\x01 \x03(\tR\x08tradeDay\x12$\n\x0ehalf_trade_day\x18\x02 \x03(\tR\x0chalfTradeDay\"4\n\x1a\x43\x61pitalFlowIntradayRequest\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\"\xef\x01\n\x1b\x43\x61pitalFlowIntradayResponse\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12o\n\x12\x63\x61pital_flow_lines\x18\x02 \x03(\x0b\x32\x41.longportapp.quote.v1.CapitalFlowIntradayResponse.CapitalFlowLineR\x10\x63\x61pitalFlowLines\x1aG\n\x0f\x43\x61pitalFlowLine\x12\x16\n\x06inflow\x18\x01 \x01(\tR\x06inflow\x12\x1c\n\ttimestamp\x18\x02 \x01(\x03R\ttimestamp\"\xfc\x02\n\x1b\x43\x61pitalDistributionResponse\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x1c\n\ttimestamp\x18\x02 \x01(\x03R\ttimestamp\x12\x64\n\ncapital_in\x18\x03 \x01(\x0b\x32\x45.longportapp.quote.v1.CapitalDistributionResponse.CapitalDistributionR\tcapitalIn\x12\x66\n\x0b\x63\x61pital_out\x18\x04 \x01(\x0b\x32\x45.longportapp.quote.v1.CapitalDistributionResponse.CapitalDistributionR\ncapitalOut\x1aY\n\x13\x43\x61pitalDistribution\x12\x14\n\x05large\x18\x01 \x01(\tR\x05large\x12\x16\n\x06medium\x18\x02 \x01(\tR\x06medium\x12\x14\n\x05small\x18\x03 \x01(\tR\x05small\"t\n\x18SecurityCalcQuoteRequest\x12\x18\n\x07symbols\x18\x01 \x03(\tR\x07symbols\x12>\n\ncalc_index\x18\x02 \x03(\x0e\x32\x1f.longportapp.quote.v1.CalcIndexR\tcalcIndex\"\xc5\x0b\n\x11SecurityCalcIndex\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x1b\n\tlast_done\x18\x02 \x01(\tR\x08lastDone\x12\x1d\n\nchange_val\x18\x03 \x01(\tR\tchangeVal\x12\x1f\n\x0b\x63hange_rate\x18\x04 \x01(\tR\nchangeRate\x12\x16\n\x06volume\x18\x05 \x01(\x03R\x06volume\x12\x1a\n\x08turnover\x18\x06 \x01(\tR\x08turnover\x12&\n\x0fytd_change_rate\x18\x07 \x01(\tR\rytdChangeRate\x12#\n\rturnover_rate\x18\x08 \x01(\tR\x0cturnoverRate\x12,\n\x12total_market_value\x18\t \x01(\tR\x10totalMarketValue\x12!\n\x0c\x63\x61pital_flow\x18\n \x01(\tR\x0b\x63\x61pitalFlow\x12\x1c\n\tamplitude\x18\x0b \x01(\tR\tamplitude\x12!\n\x0cvolume_ratio\x18\x0c \x01(\tR\x0bvolumeRatio\x12 \n\x0cpe_ttm_ratio\x18\r \x01(\tR\npeTtmRatio\x12\x19\n\x08pb_ratio\x18\x0e \x01(\tR\x07pbRatio\x12,\n\x12\x64ividend_ratio_ttm\x18\x0f \x01(\tR\x10\x64ividendRatioTtm\x12/\n\x14\x66ive_day_change_rate\x18\x10 \x01(\tR\x11\x66iveDayChangeRate\x12-\n\x13ten_day_change_rate\x18\x11 \x01(\tR\x10tenDayChangeRate\x12\x31\n\x15half_year_change_rate\x18\x12 \x01(\tR\x12halfYearChangeRate\x12\x37\n\x18\x66ive_minutes_change_rate\x18\x13 \x01(\tR\x15\x66iveMinutesChangeRate\x12\x1f\n\x0b\x65xpiry_date\x18\x14 \x01(\tR\nexpiryDate\x12!\n\x0cstrike_price\x18\x15 \x01(\tR\x0bstrikePrice\x12,\n\x12upper_strike_price\x18\x16 \x01(\tR\x10upperStrikePrice\x12,\n\x12lower_strike_price\x18\x17 \x01(\tR\x10lowerStrikePrice\x12\'\n\x0foutstanding_qty\x18\x18 \x01(\x03R\x0eoutstandingQty\x12+\n\x11outstanding_ratio\x18\x19 \x01(\tR\x10outstandingRatio\x12\x18\n\x07premium\x18\x1a \x01(\tR\x07premium\x12\x17\n\x07itm_otm\x18\x1b \x01(\tR\x06itmOtm\x12-\n\x12implied_volatility\x18\x1c \x01(\tR\x11impliedVolatility\x12#\n\rwarrant_delta\x18\x1d \x01(\tR\x0cwarrantDelta\x12\x1d\n\ncall_price\x18\x1e \x01(\tR\tcallPrice\x12\"\n\rto_call_price\x18\x1f \x01(\tR\x0btoCallPrice\x12-\n\x12\x65\x66\x66\x65\x63tive_leverage\x18  \x01(\tR\x11\x65\x66\x66\x65\x63tiveLeverage\x12%\n\x0eleverage_ratio\x18! \x01(\tR\rleverageRatio\x12)\n\x10\x63onversion_ratio\x18\" \x01(\tR\x0f\x63onversionRatio\x12#\n\rbalance_point\x18# \x01(\tR\x0c\x62\x61lancePoint\x12#\n\ropen_interest\x18$ \x01(\x03R\x0copenInterest\x12\x14\n\x05\x64\x65lta\x18% \x01(\tR\x05\x64\x65lta\x12\x14\n\x05gamma\x18& \x01(\tR\x05gamma\x12\x14\n\x05theta\x18\' \x01(\tR\x05theta\x12\x12\n\x04vega\x18( \x01(\tR\x04vega\x12\x10\n\x03rho\x18) \x01(\tR\x03rho\"t\n\x19SecurityCalcQuoteResponse\x12W\n\x13security_calc_index\x18\x01 \x03(\x0b\x32\'.longportapp.quote.v1.SecurityCalcIndexR\x11securityCalcIndex\"\xb0\x05\n!SecurityHistoryCandlestickRequest\x12\x16\n\x06symbol\x18\x01 \x01(\tR\x06symbol\x12\x34\n\x06period\x18\x02 \x01(\x0e\x32\x1c.longportapp.quote.v1.PeriodR\x06period\x12\x41\n\x0b\x61\x64just_type\x18\x03 \x01(\x0e\x32 .longportapp.quote.v1.AdjustTypeR\nadjustType\x12P\n\nquery_type\x18\x04 \x01(\x0e\x32\x31.longportapp.quote.v1.HistoryCandlestickQueryTypeR\tqueryType\x12j\n\x0eoffset_request\x18\x05 \x01(\x0b\x32\x43.longportapp.quote.v1.SecurityHistoryCandlestickRequest.OffsetQueryR\roffsetRequest\x12\x64\n\x0c\x64\x61te_request\x18\x06 \x01(\x0b\x32\x41.longportapp.quote.v1.SecurityHistoryCandlestickRequest.DateQueryR\x0b\x64\x61teRequest\x1a\x8e\x01\n\x0bOffsetQuery\x12=\n\tdirection\x18\x01 \x01(\x0e\x32\x1f.longportapp.quote.v1.DirectionR\tdirection\x12\x12\n\x04\x64\x61te\x18\x02 \x01(\tR\x04\x64\x61te\x12\x16\n\x06minute\x18\x03 \x01(\tR\x06minute\x12\x14\n\x05\x63ount\x18\x04 \x01(\x05R\x05\x63ount\x1a\x45\n\tDateQuery\x12\x1d\n\nstart_date\x18\x01 \x01(\tR\tstartDate\x12\x19\n\x08\x65nd_date\x18\x02 \x01(\tR\x07\x65ndDate\"\x19\n\x17UserQuoteProfileRequest\"p\n\tRateLimit\x12\x37\n\x07\x63ommand\x18\x01 \x01(\x0e\x32\x1d.longportapp.quote.v1.CommandR\x07\x63ommand\x12\x14\n\x05limit\x18\x02 \x01(\x05R\x05limit\x12\x14\n\x05\x62urst\x18\x03 \x01(\x05R\x05\x62urst\"\xfd\x01\n\x18UserQuoteProfileResponse\x12\x1b\n\tmember_id\x18\x01 \x01(\x03R\x08memberId\x12\x1f\n\x0bquote_level\x18\x02 \x01(\tR\nquoteLevel\x12\'\n\x0fsubscribe_limit\x18\x03 \x01(\x05R\x0esubscribeLimit\x12:\n\x19history_candlestick_limit\x18\x04 \x01(\x05R\x17historyCandlestickLimit\x12>\n\nrate_limit\x18\x05 \x03(\x0b\x32\x1f.longportapp.quote.v1.RateLimitR\trateLimit*\xe2\x05\n\x07\x43ommand\x12\x13\n\x0fUNKNOWN_COMMAND\x10\x00\x12\x0e\n\nHEART_BEAT\x10\x01\x12\x08\n\x04\x41UTH\x10\x02\x12\r\n\tRECONNECT\x10\x03\x12\x19\n\x15QueryUserQuoteProfile\x10\x04\x12\x10\n\x0cSubscription\x10\x05\x12\r\n\tSubscribe\x10\x06\x12\x0f\n\x0bUnsubscribe\x10\x07\x12\x1a\n\x16QueryMarketTradePeriod\x10\x08\x12\x17\n\x13QueryMarketTradeDay\x10\t\x12\x1b\n\x17QuerySecurityStaticInfo\x10\n\x12\x16\n\x12QuerySecurityQuote\x10\x0b\x12\x14\n\x10QueryOptionQuote\x10\x0c\x12\x15\n\x11QueryWarrantQuote\x10\r\x12\x0e\n\nQueryDepth\x10\x0e\x12\x10\n\x0cQueryBrokers\x10\x0f\x12\x1d\n\x19QueryParticipantBrokerIds\x10\x10\x12\x0e\n\nQueryTrade\x10\x11\x12\x11\n\rQueryIntraday\x10\x12\x12\x14\n\x10QueryCandlestick\x10\x13\x12\x18\n\x14QueryOptionChainDate\x10\x14\x12\"\n\x1eQueryOptionChainDateStrikeInfo\x10\x15\x12\x1a\n\x16QueryWarrantIssuerInfo\x10\x16\x12\x1a\n\x16QueryWarrantFilterList\x10\x17\x12\x1c\n\x18QueryCapitalFlowIntraday\x10\x18\x12 \n\x1cQueryCapitalFlowDistribution\x10\x19\x12\x1a\n\x16QuerySecurityCalcIndex\x10\x1a\x12\x1b\n\x17QueryHistoryCandlestick\x10\x1b\x12\x11\n\rPushQuoteData\x10\x65\x12\x11\n\rPushDepthData\x10\x66\x12\x13\n\x0fPushBrokersData\x10g\x12\x11\n\rPushTradeData\x10h*\xc2\x01\n\x0bTradeStatus\x12\n\n\x06NORMAL\x10\x00\x12\n\n\x06HALTED\x10\x01\x12\x0c\n\x08\x44\x45LISTED\x10\x02\x12\x08\n\x04\x46USE\x10\x03\x12\x10\n\x0cPREPARE_LIST\x10\x04\x12\x0e\n\nCODE_MOVED\x10\x05\x12\x10\n\x0cTO_BE_OPENED\x10\x06\x12\x15\n\x11SPLIT_STOCK_HALTS\x10\x07\x12\x0b\n\x07\x45XPIRED\x10\x08\x12\x18\n\x14WARRANT_PREPARE_LIST\x10\t\x12\x11\n\rSUSPEND_TRADE\x10\n*?\n\x0cTradeSession\x12\x10\n\x0cNORMAL_TRADE\x10\x00\x12\r\n\tPRE_TRADE\x10\x01\x12\x0e\n\nPOST_TRADE\x10\x02*/\n\nAdjustType\x12\r\n\tNO_ADJUST\x10\x00\x12\x12\n\x0e\x46ORWARD_ADJUST\x10\x01*\xa2\x01\n\x06Period\x12\x12\n\x0eUNKNOWN_PERIOD\x10\x00\x12\x0e\n\nONE_MINUTE\x10\x01\x12\x0f\n\x0b\x46IVE_MINUTE\x10\x05\x12\x12\n\x0e\x46IFTEEN_MINUTE\x10\x0f\x12\x11\n\rTHIRTY_MINUTE\x10\x1e\x12\x10\n\x0cSIXTY_MINUTE\x10<\x12\x08\n\x03\x44\x41Y\x10\xe8\x07\x12\t\n\x04WEEK\x10\xd0\x0f\x12\n\n\x05MONTH\x10\xb8\x17\x12\t\n\x04YEAR\x10\xa0\x1f*I\n\x07SubType\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\t\n\x05QUOTE\x10\x01\x12\t\n\x05\x44\x45PTH\x10\x02\x12\x0b\n\x07\x42ROKERS\x10\x03\x12\t\n\x05TRADE\x10\x04*#\n\x0cPushQuoteTag\x12\n\n\x06Normal\x10\x00\x12\x07\n\x03\x45od\x10\x01*\x96\t\n\tCalcIndex\x12\x15\n\x11\x43\x41LCINDEX_UNKNOWN\x10\x00\x12\x17\n\x13\x43\x41LCINDEX_LAST_DONE\x10\x01\x12\x18\n\x14\x43\x41LCINDEX_CHANGE_VAL\x10\x02\x12\x19\n\x15\x43\x41LCINDEX_CHANGE_RATE\x10\x03\x12\x14\n\x10\x43\x41LCINDEX_VOLUME\x10\x04\x12\x16\n\x12\x43\x41LCINDEX_TURNOVER\x10\x05\x12\x1d\n\x19\x43\x41LCINDEX_YTD_CHANGE_RATE\x10\x06\x12\x1b\n\x17\x43\x41LCINDEX_TURNOVER_RATE\x10\x07\x12 \n\x1c\x43\x41LCINDEX_TOTAL_MARKET_VALUE\x10\x08\x12\x1a\n\x16\x43\x41LCINDEX_CAPITAL_FLOW\x10\t\x12\x17\n\x13\x43\x41LCINDEX_AMPLITUDE\x10\n\x12\x1a\n\x16\x43\x41LCINDEX_VOLUME_RATIO\x10\x0b\x12\x1a\n\x16\x43\x41LCINDEX_PE_TTM_RATIO\x10\x0c\x12\x16\n\x12\x43\x41LCINDEX_PB_RATIO\x10\r\x12 \n\x1c\x43\x41LCINDEX_DIVIDEND_RATIO_TTM\x10\x0e\x12\"\n\x1e\x43\x41LCINDEX_FIVE_DAY_CHANGE_RATE\x10\x0f\x12!\n\x1d\x43\x41LCINDEX_TEN_DAY_CHANGE_RATE\x10\x10\x12#\n\x1f\x43\x41LCINDEX_HALF_YEAR_CHANGE_RATE\x10\x11\x12&\n\"CALCINDEX_FIVE_MINUTES_CHANGE_RATE\x10\x12\x12\x19\n\x15\x43\x41LCINDEX_EXPIRY_DATE\x10\x13\x12\x1a\n\x16\x43\x41LCINDEX_STRIKE_PRICE\x10\x14\x12 \n\x1c\x43\x41LCINDEX_UPPER_STRIKE_PRICE\x10\x15\x12 \n\x1c\x43\x41LCINDEX_LOWER_STRIKE_PRICE\x10\x16\x12\x1d\n\x19\x43\x41LCINDEX_OUTSTANDING_QTY\x10\x17\x12\x1f\n\x1b\x43\x41LCINDEX_OUTSTANDING_RATIO\x10\x18\x12\x15\n\x11\x43\x41LCINDEX_PREMIUM\x10\x19\x12\x15\n\x11\x43\x41LCINDEX_ITM_OTM\x10\x1a\x12 \n\x1c\x43\x41LCINDEX_IMPLIED_VOLATILITY\x10\x1b\x12\x1b\n\x17\x43\x41LCINDEX_WARRANT_DELTA\x10\x1c\x12\x18\n\x14\x43\x41LCINDEX_CALL_PRICE\x10\x1d\x12\x1b\n\x17\x43\x41LCINDEX_TO_CALL_PRICE\x10\x1e\x12 \n\x1c\x43\x41LCINDEX_EFFECTIVE_LEVERAGE\x10\x1f\x12\x1c\n\x18\x43\x41LCINDEX_LEVERAGE_RATIO\x10 \x12\x1e\n\x1a\x43\x41LCINDEX_CONVERSION_RATIO\x10!\x12\x1b\n\x17\x43\x41LCINDEX_BALANCE_POINT\x10\"\x12\x1b\n\x17\x43\x41LCINDEX_OPEN_INTEREST\x10#\x12\x13\n\x0f\x43\x41LCINDEX_DELTA\x10$\x12\x13\n\x0f\x43\x41LCINDEX_GAMMA\x10%\x12\x13\n\x0f\x43\x41LCINDEX_THETA\x10&\x12\x12\n\x0e\x43\x41LCINDEX_VEGA\x10\'\x12\x11\n\rCALCINDEX_RHO\x10(*]\n\x1bHistoryCandlestickQueryType\x12\x16\n\x12UNKNOWN_QUERY_TYPE\x10\x00\x12\x13\n\x0fQUERY_BY_OFFSET\x10\x01\x12\x11\n\rQUERY_BY_DATE\x10\x02*&\n\tDirection\x12\x0c\n\x08\x42\x41\x43KWARD\x10\x00\x12\x0b\n\x07\x46ORWARD\x10\x01\x42\xd5\x01\n\x18\x63om.longportapp.quote.v1B\x08\x41piProtoP\x01Z=github.com/longportapp/openapi-protobufs/gen/go/quote;quotev1\xa2\x02\x03LQX\xaa\x02\x14Longportapp.Quote.V1\xca\x02\x14Longportapp\\Quote\\V1\xe2\x02 Longportapp\\Quote\\V1\\GPBMetadata\xea\x02\x16Longportapp::Quote::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'quote.api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.longportapp.quote.v1B\010ApiProtoP\001Z=github.com/longportapp/openapi-protobufs/gen/go/quote;quotev1\242\002\003LQX\252\002\024Longportapp.Quote.V1\312\002\024Longportapp\\Quote\\V1\342\002 Longportapp\\Quote\\V1\\GPBMetadata\352\002\026Longportapp::Quote::V1'
  _globals['_COMMAND']._serialized_start=12957
  _globals['_COMMAND']._serialized_end=13695
  _globals['_TRADESTATUS']._serialized_start=13698
  _globals['_TRADESTATUS']._serialized_end=13892
  _globals['_TRADESESSION']._serialized_start=13894
  _globals['_TRADESESSION']._serialized_end=13957
  _globals['_ADJUSTTYPE']._serialized_start=13959
  _globals['_ADJUSTTYPE']._serialized_end=14006
  _globals['_PERIOD']._serialized_start=14009
  _globals['_PERIOD']._serialized_end=14171
  _globals['_SUBTYPE']._serialized_start=14173
  _globals['_SUBTYPE']._serialized_end=14246
  _globals['_PUSHQUOTETAG']._serialized_start=14248
  _globals['_PUSHQUOTETAG']._serialized_end=14283
  _globals['_CALCINDEX']._serialized_start=14286
  _globals['_CALCINDEX']._serialized_end=15460
  _globals['_HISTORYCANDLESTICKQUERYTYPE']._serialized_start=15462
  _globals['_HISTORYCANDLESTICKQUERYTYPE']._serialized_end=15555
  _globals['_DIRECTION']._serialized_start=15557
  _globals['_DIRECTION']._serialized_end=15595
  _globals['_SECURITYREQUEST']._serialized_start=41
  _globals['_SECURITYREQUEST']._serialized_end=82
  _globals['_MULTISECURITYREQUEST']._serialized_start=84
  _globals['_MULTISECURITYREQUEST']._serialized_end=130
  _globals['_SECURITYSTATICINFORESPONSE']._serialized_start=132
  _globals['_SECURITYSTATICINFORESPONSE']._serialized_end=236
  _globals['_STATICINFO']._serialized_start=239
  _globals['_STATICINFO']._serialized_end=746
  _globals['_SECURITYQUOTERESPONSE']._serialized_start=748
  _globals['_SECURITYQUOTERESPONSE']._serialized_end=839
  _globals['_SECURITYQUOTE']._serialized_start=842
  _globals['_SECURITYQUOTE']._serialized_end=1309
  _globals['_PREPOSTQUOTE']._serialized_start=1312
  _globals['_PREPOSTQUOTE']._serialized_end=1506
  _globals['_OPTIONQUOTERESPONSE']._serialized_start=1508
  _globals['_OPTIONQUOTERESPONSE']._serialized_end=1595
  _globals['_OPTIONQUOTE']._serialized_start=1598
  _globals['_OPTIONQUOTE']._serialized_end=1978
  _globals['_OPTIONEXTEND']._serialized_start=1981
  _globals['_OPTIONEXTEND']._serialized_end=2398
  _globals['_WARRANTQUOTERESPONSE']._serialized_start=2400
  _globals['_WARRANTQUOTERESPONSE']._serialized_end=2489
  _globals['_WARRANTQUOTE']._serialized_start=2492
  _globals['_WARRANTQUOTE']._serialized_end=2876
  _globals['_WARRANTEXTEND']._serialized_start=2879
  _globals['_WARRANTEXTEND']._serialized_end=3374
  _globals['_SECURITYDEPTHRESPONSE']._serialized_start=3377
  _globals['_SECURITYDEPTHRESPONSE']._serialized_end=3518
  _globals['_DEPTH']._serialized_start=3520
  _globals['_DEPTH']._serialized_end=3630
  _globals['_SECURITYBROKERSRESPONSE']._serialized_start=3633
  _globals['_SECURITYBROKERSRESPONSE']._serialized_end=3810
  _globals['_BROKERS']._serialized_start=3812
  _globals['_BROKERS']._serialized_end=3880
  _globals['_PARTICIPANTBROKERIDSRESPONSE']._serialized_start=3883
  _globals['_PARTICIPANTBROKERIDSRESPONSE']._serialized_end=4014
  _globals['_PARTICIPANTINFO']._serialized_start=4017
  _globals['_PARTICIPANTINFO']._serialized_end=4209
  _globals['_SECURITYTRADEREQUEST']._serialized_start=4211
  _globals['_SECURITYTRADEREQUEST']._serialized_end=4279
  _globals['_SECURITYTRADERESPONSE']._serialized_start=4281
  _globals['_SECURITYTRADERESPONSE']._serialized_end=4381
  _globals['_TRADE']._serialized_start=4384
  _globals['_TRADE']._serialized_end=4601
  _globals['_SECURITYINTRADAYREQUEST']._serialized_start=4603
  _globals['_SECURITYINTRADAYREQUEST']._serialized_end=4652
  _globals['_SECURITYINTRADAYRESPONSE']._serialized_start=4654
  _globals['_SECURITYINTRADAYRESPONSE']._serialized_end=4754
  _globals['_LINE']._serialized_start=4757
  _globals['_LINE']._serialized_end=4896
  _globals['_SECURITYCANDLESTICKREQUEST']._serialized_start=4899
  _globals['_SECURITYCANDLESTICKREQUEST']._serialized_end=5094
  _globals['_SECURITYCANDLESTICKRESPONSE']._serialized_start=5096
  _globals['_SECURITYCANDLESTICKRESPONSE']._serialized_end=5220
  _globals['_CANDLESTICK']._serialized_start=5223
  _globals['_CANDLESTICK']._serialized_end=5398
  _globals['_OPTIONCHAINDATELISTRESPONSE']._serialized_start=5400
  _globals['_OPTIONCHAINDATELISTRESPONSE']._serialized_end=5462
  _globals['_OPTIONCHAINDATESTRIKEINFOREQUEST']._serialized_start=5464
  _globals['_OPTIONCHAINDATESTRIKEINFOREQUEST']._serialized_end=5555
  _globals['_OPTIONCHAINDATESTRIKEINFORESPONSE']._serialized_start=5557
  _globals['_OPTIONCHAINDATESTRIKEINFORESPONSE']._serialized_end=5675
  _globals['_STRIKEPRICEINFO']._serialized_start=5678
  _globals['_STRIKEPRICEINFO']._serialized_end=5809
  _globals['_ISSUERINFORESPONSE']._serialized_start=5811
  _globals['_ISSUERINFORESPONSE']._serialized_end=5898
  _globals['_ISSUERINFO']._serialized_start=5900
  _globals['_ISSUERINFO']._serialized_end=6003
  _globals['_WARRANTFILTERLISTREQUEST']._serialized_start=6006
  _globals['_WARRANTFILTERLISTREQUEST']._serialized_end=6157
  _globals['_FILTERCONFIG']._serialized_start=6160
  _globals['_FILTERCONFIG']._serialized_end=6426
  _globals['_WARRANTFILTERLISTRESPONSE']._serialized_start=6429
  _globals['_WARRANTFILTERLISTRESPONSE']._serialized_end=6561
  _globals['_FILTERWARRANT']._serialized_start=6564
  _globals['_FILTERWARRANT']._serialized_end=7411
  _globals['_MARKETTRADEPERIODRESPONSE']._serialized_start=7413
  _globals['_MARKETTRADEPERIODRESPONSE']._serialized_end=7531
  _globals['_MARKETTRADEPERIOD']._serialized_start=7533
  _globals['_MARKETTRADEPERIOD']._serialized_end=7648
  _globals['_TRADEPERIOD']._serialized_start=7651
  _globals['_TRADEPERIOD']._serialized_end=7791
  _globals['_SUBSCRIPTIONREQUEST']._serialized_start=7793
  _globals['_SUBSCRIPTIONREQUEST']._serialized_end=7814
  _globals['_SUBSCRIPTIONRESPONSE']._serialized_start=7816
  _globals['_SUBSCRIPTIONRESPONSE']._serialized_end=7900
  _globals['_SUBTYPELIST']._serialized_start=7902
  _globals['_SUBTYPELIST']._serialized_end=7997
  _globals['_SUBSCRIBEREQUEST']._serialized_start=8000
  _globals['_SUBSCRIBEREQUEST']._serialized_end=8136
  _globals['_UNSUBSCRIBEREQUEST']._serialized_start=8139
  _globals['_UNSUBSCRIBEREQUEST']._serialized_end=8270
  _globals['_UNSUBSCRIBERESPONSE']._serialized_start=8272
  _globals['_UNSUBSCRIBERESPONSE']._serialized_end=8293
  _globals['_PUSHQUOTE']._serialized_start=8296
  _globals['_PUSHQUOTE']._serialized_end=8807
  _globals['_PUSHDEPTH']._serialized_start=8810
  _globals['_PUSHDEPTH']._serialized_end=8967
  _globals['_PUSHBROKERS']._serialized_start=8970
  _globals['_PUSHBROKERS']._serialized_end=9163
  _globals['_PUSHTRADE']._serialized_start=9165
  _globals['_PUSHTRADE']._serialized_end=9279
  _globals['_MARKETTRADEDAYREQUEST']._serialized_start=9281
  _globals['_MARKETTRADEDAYREQUEST']._serialized_end=9378
  _globals['_MARKETTRADEDAYRESPONSE']._serialized_start=9380
  _globals['_MARKETTRADEDAYRESPONSE']._serialized_end=9471
  _globals['_CAPITALFLOWINTRADAYREQUEST']._serialized_start=9473
  _globals['_CAPITALFLOWINTRADAYREQUEST']._serialized_end=9525
  _globals['_CAPITALFLOWINTRADAYRESPONSE']._serialized_start=9528
  _globals['_CAPITALFLOWINTRADAYRESPONSE']._serialized_end=9767
  _globals['_CAPITALFLOWINTRADAYRESPONSE_CAPITALFLOWLINE']._serialized_start=9696
  _globals['_CAPITALFLOWINTRADAYRESPONSE_CAPITALFLOWLINE']._serialized_end=9767
  _globals['_CAPITALDISTRIBUTIONRESPONSE']._serialized_start=9770
  _globals['_CAPITALDISTRIBUTIONRESPONSE']._serialized_end=10150
  _globals['_CAPITALDISTRIBUTIONRESPONSE_CAPITALDISTRIBUTION']._serialized_start=10061
  _globals['_CAPITALDISTRIBUTIONRESPONSE_CAPITALDISTRIBUTION']._serialized_end=10150
  _globals['_SECURITYCALCQUOTEREQUEST']._serialized_start=10152
  _globals['_SECURITYCALCQUOTEREQUEST']._serialized_end=10268
  _globals['_SECURITYCALCINDEX']._serialized_start=10271
  _globals['_SECURITYCALCINDEX']._serialized_end=11748
  _globals['_SECURITYCALCQUOTERESPONSE']._serialized_start=11750
  _globals['_SECURITYCALCQUOTERESPONSE']._serialized_end=11866
  _globals['_SECURITYHISTORYCANDLESTICKREQUEST']._serialized_start=11869
  _globals['_SECURITYHISTORYCANDLESTICKREQUEST']._serialized_end=12557
  _globals['_SECURITYHISTORYCANDLESTICKREQUEST_OFFSETQUERY']._serialized_start=12344
  _globals['_SECURITYHISTORYCANDLESTICKREQUEST_OFFSETQUERY']._serialized_end=12486
  _globals['_SECURITYHISTORYCANDLESTICKREQUEST_DATEQUERY']._serialized_start=12488
  _globals['_SECURITYHISTORYCANDLESTICKREQUEST_DATEQUERY']._serialized_end=12557
  _globals['_USERQUOTEPROFILEREQUEST']._serialized_start=12559
  _globals['_USERQUOTEPROFILEREQUEST']._serialized_end=12584
  _globals['_RATELIMIT']._serialized_start=12586
  _globals['_RATELIMIT']._serialized_end=12698
  _globals['_USERQUOTEPROFILERESPONSE']._serialized_start=12701
  _globals['_USERQUOTEPROFILERESPONSE']._serialized_end=12954
# @@protoc_insertion_point(module_scope)
