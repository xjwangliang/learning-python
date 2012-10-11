package com.taobao.api.request;

import com.taobao.api.internal.util.RequestCheckUtils;
import java.util.Map;

import com.taobao.api.TaobaoRequest;
import com.taobao.api.internal.util.TaobaoHashMap;
import com.taobao.api.response.TaobaokeUrlConvertResponse;
import com.taobao.api.ApiRuleException;
/**
 * TOP API: taobao.taobaoke.url.convert request
 * 
 * @author auto create
 * @since 1.0, 2012-09-23 16:40:16
 */
public class TaobaokeUrlConvertRequest implements TaobaoRequest<TaobaokeUrlConvertResponse> {

	private TaobaoHashMap udfParams; // add user-defined text parameters
	private Long timestamp;

	/** 
	* 自定义输入串.格式:英文和数字组成;长度不能大于12个字符,区分不同的推广渠道,如:bbs,表示bbs为推广渠道;blog,表示blog为推广渠道
	 */
	private String outerCode;

	/** 
	* 需要转化为淘客链接的url
	 */
	private String url;

	public void setOuterCode(String outerCode) {
		this.outerCode = outerCode;
	}
	public String getOuterCode() {
		return this.outerCode;
	}

	public void setUrl(String url) {
		this.url = url;
	}
	public String getUrl() {
		return this.url;
	}

	public Long getTimestamp() {
		return this.timestamp;
	}

	public void setTimestamp(Long timestamp) {
		this.timestamp = timestamp;
	}

	public String getApiMethodName() {
		return "taobao.taobaoke.url.convert";
	}

	public Map<String, String> getTextParams() {		
		TaobaoHashMap txtParams = new TaobaoHashMap();
		txtParams.put("outer_code", this.outerCode);
		txtParams.put("url", this.url);
		if(this.udfParams != null) {
			txtParams.putAll(this.udfParams);
		}
		return txtParams;
	}

	public void putOtherTextParam(String key, String value) {
		if(this.udfParams == null) {
			this.udfParams = new TaobaoHashMap();
		}
		this.udfParams.put(key, value);
	}

	public Class<TaobaokeUrlConvertResponse> getResponseClass() {
		return TaobaokeUrlConvertResponse.class;
	}

	public void check() throws ApiRuleException {
		
		RequestCheckUtils.checkNotEmpty(url,"url");
	}
}
